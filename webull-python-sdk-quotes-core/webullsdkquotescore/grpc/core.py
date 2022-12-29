# Copyright 2022 Webull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8

import collections
import datetime
import logging
import queue as queue_module
import threading
import time

from webullsdkquotescore.grpc import grpc_signature_composer as composer

_LOGGER = logging.getLogger(__name__)
_BIDIRECTIONAL_CONSUMER_NAME = "Thread-Async-grpc-conn-worker"


class _RequestQueueGenerator(object):
    def __init__(self, queue, period=1, initial_request=None):
        self._queue = queue
        self._period = period
        self._initial_request = initial_request
        self.call = None

    def _is_active(self):
        if self.call is not None and not self.call.is_active():
            return False
        else:
            return True

    def __iter__(self):
        if self._initial_request is not None:
            if callable(self._initial_request):
                yield self._initial_request()
            else:
                yield self._initial_request

        while True:
            try:
                item = self._queue.get()
            except queue_module.Empty:
                if not self._is_active():
                    _LOGGER.debug("Empty queue and inactive call, exiting request generator.")
                    return
                else:
                    _LOGGER.debug("Enter the continue")
                    continue

            if item is None:
                _LOGGER.debug("Cleanly exiting request generator.")
                return

            if not self._is_active():
                self._queue.put(item)
                _LOGGER.debug(
                    "Inactive call, replacing item on queue and exiting "
                    "request generator."
                )
                return

            yield item


class _Throttle(object):
    def __init__(self, access_limit, time_window):
        if access_limit < 1:
            raise ValueError("access_limit argument must be positive")

        if time_window <= datetime.timedelta(0):
            raise ValueError("time_window argument must be a positive timedelta")

        self._time_window = time_window
        self._access_limit = access_limit
        self._past_entries = collections.deque(
            maxlen=access_limit
        )  # least recent first
        self._entry_lock = threading.Lock()

    def __enter__(self):
        with self._entry_lock:
            cutoff_time = datetime.datetime.now() - self._time_window

            while self._past_entries and self._past_entries[0] < cutoff_time:
                self._past_entries.popleft()

            if len(self._past_entries) < self._access_limit:
                self._past_entries.append(datetime.datetime.now())
                return 0.0  # no waiting was needed

            to_wait = (self._past_entries[0] - cutoff_time).total_seconds()
            time.sleep(to_wait)

            self._past_entries.append(datetime.datetime.now())
            return to_wait

    def __repr__(self):
        return "{}(access_limit={}, time_window={})".format(
            self.__class__.__name__, self._access_limit, repr(self._time_window)
        )


class BidiRpc(object):

    def __init__(self,
                 start_rpc,
                 app_key,
                 app_secret,
                 host,
                 stream_uri,
                 initial_request=None):
        self._start_rpc = start_rpc
        self._initial_request = initial_request
        self._request_queue = queue_module.Queue()
        self._request_generator = None
        self._is_active = False
        self._callbacks = []
        self.call = None
        self._app_key = app_key
        self._app_secret = app_secret
        self._host = host
        self._stream_uri = stream_uri

    def add_done_callback(self, callback):
        self._callbacks.append(callback)

    def _on_call_done(self, future):
        for callback in self._callbacks:
            callback(future)

    def open(self):
        if self.is_active:
            raise ValueError("Can not open an already open stream.")

        request_generator = _RequestQueueGenerator(
            self._request_queue, initial_request=self._initial_request
        )

        signature, metadata = composer.calc_signature(self._app_key, self._app_secret, self._host, self._stream_uri,
                                                      None)

        call = self._start_rpc(iter(request_generator), metadata=metadata)

        request_generator.call = call

        if hasattr(call, "_wrapped"):
            call._wrapped.add_done_callback(self._on_call_done)
        else:
            call.add_done_callback(self._on_call_done)

        self._request_generator = request_generator
        self.call = call

    def close(self):
        if self.call is None:
            return

        self._request_queue.put(None)
        self.call.cancel()
        self._request_generator = None

    def send(self, request):
        if self.call is None:
            raise ValueError("Can not send() on an RPC that has never been open()ed.")

        if self.call.is_active():
            self._request_queue.put(request)
        else:
            next(self.call)

    def recv(self):
        if self.call is None:
            raise ValueError("Can not recv() on an RPC that has never been open()ed.")

        return next(self.call)

    @property
    def is_active(self):
        return self.call is not None and self.call.is_active()

    @property
    def pending_requests(self):
        return self._request_queue.qsize()


def _never_terminate(future_or_error):
    return False


class ResumableBidiRpc(BidiRpc):
    def __init__(
            self,
            app_key,
            app_secret,
            host,
            stream_uri,
            start_rpc,
            should_recover,
            should_terminate=_never_terminate,
            initial_request=None,
            throttle_reopen=False,
    ):
        super(ResumableBidiRpc, self).__init__(start_rpc, app_key, app_secret, host, stream_uri,
                                               initial_request)
        self._should_recover = should_recover
        self._should_terminate = should_terminate
        self._operational_lock = threading.RLock()
        self._finalized = False
        self._finalize_lock = threading.Lock()

        if throttle_reopen:
            self._reopen_throttle = _Throttle(
                access_limit=5, time_window=datetime.timedelta(seconds=10)
            )
        else:
            self._reopen_throttle = None

    def _finalize(self, result):
        with self._finalize_lock:
            if self._finalized:
                return

            for callback in self._callbacks:
                callback(result)

            self._finalized = True

    def _on_call_done(self, future):
        with self._operational_lock:
            if self._should_terminate(future):
                self._finalize(future)
            elif not self._should_recover(future):
                self._finalize(future)
            else:
                _LOGGER.debug("Re-opening stream from gRPC callback.")
                self._reopen()

    def _reopen(self):
        with self._operational_lock:
            if self.call is not None and self.call.is_active():
                _LOGGER.debug("Stream was already re-established.")
                return

            self.call = None
            self._request_generator = None
            try:
                if self._reopen_throttle:
                    with self._reopen_throttle:
                        self.open()
                else:
                    self.open()
            except Exception as exc:
                _LOGGER.debug("Failed to re-open stream due to %s", exc)
                self._finalize(exc)
                raise

            _LOGGER.info("Re-established stream")

    def _recoverable(self, method, *args, **kwargs):
        while True:
            try:
                return method(*args, **kwargs)

            except Exception as exc:
                with self._operational_lock:
                    _LOGGER.debug("Call to retryable %r caused %s.", method, exc)

                    if self._should_terminate(exc):
                        self.close()
                        _LOGGER.debug("Terminating %r due to %s.", method, exc)
                        self._finalize(exc)
                        break

                    if not self._should_recover(exc):
                        self.close()
                        _LOGGER.debug("Not retrying %r due to %s.", method, exc)
                        self._finalize(exc)
                        raise exc

                    _LOGGER.debug("Re-opening stream from retryable %r.", method)
                    self._reopen()

    def _send(self, request):
        self._request_queue.put(request)

    def send(self, request):
        return self._recoverable(self._send, request)

    def _recv(self):
        with self._operational_lock:
            call = self.call

        if call is None:
            raise ValueError("Can not recv() on an RPC that has never been open()ed.")

        return next(call)

    def recv(self):
        return self._recoverable(self._recv)

    def close(self):
        self._finalize(None)
        super(ResumableBidiRpc, self).close()

    @property
    def is_active(self):
        with self._operational_lock:
            return self.call is not None and not self._finalized


class BackgroundConsumer(object):
    def __init__(self, bidi_rpc, on_response):
        self._bidi_rpc = bidi_rpc
        self._on_response = on_response
        self._paused = False
        self._wake = threading.Condition()
        self._thread = None
        self._operational_lock = threading.Lock()

    def _on_call_done(self, future):
        self.resume()

    def _thread_main(self, ready):
        try:
            ready.set()
            self._bidi_rpc.add_done_callback(self._on_call_done)
            self._bidi_rpc.open()

            while self._bidi_rpc.is_active:
                with self._wake:
                    while self._paused:
                        _LOGGER.debug("paused, waiting for waking.")
                        self._wake.wait()
                        _LOGGER.debug("woken.")
                _LOGGER.debug("waiting for recv.")
                response = self._bidi_rpc.recv()
                _LOGGER.debug("recved response.")
                self._on_response(response)
        except Exception as exc:
            _LOGGER.exception("%s caught unexpected exception %s and will exit.", _BIDIRECTIONAL_CONSUMER_NAME, exc)
        _LOGGER.info("%s exiting", _BIDIRECTIONAL_CONSUMER_NAME)

    def start(self, daemon=False):
        with self._operational_lock:
            ready = threading.Event()
            thread = threading.Thread(
                name=_BIDIRECTIONAL_CONSUMER_NAME,
                target=self._thread_main,
                args=(ready,),
            )
            thread.daemon = daemon
            thread.start()
            ready.wait()
            self._thread = thread
            _LOGGER.debug("Started helper thread %s", thread.name)

    def stop(self):
        with self._operational_lock:
            self._bidi_rpc.close()
            if self._thread is not None:
                self.resume()
                self._thread.join(1.0)
                if self._thread.is_alive():
                    _LOGGER.warning("Background thread did not exit.")

            self._thread = None

    @property
    def is_active(self):
        return self.active()

    def active(self):
        return self._thread is not None and self._thread.is_alive()

    def pause(self):
        with self._wake:
            self._paused = True

    def resume(self):
        with self._wake:
            self._paused = False
            self._wake.notify_all()

    @property
    def is_paused(self):
        return self._paused
