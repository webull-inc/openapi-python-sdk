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
import grpc

from webullsdkquotescore.grpc.pb import gateway_pb2 as gateway__pb2


class QuoteStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamRequest = channel.stream_stream(
                '/openapi.Quote/StreamRequest',
                request_serializer=gateway__pb2.ClientRequest.SerializeToString,
                response_deserializer=gateway__pb2.ClientResponse.FromString,
                )


class QuoteServicer(object):
    """The greeting service definition.
    """

    def StreamRequest(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuoteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamRequest': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamRequest,
                    request_deserializer=gateway__pb2.ClientRequest.FromString,
                    response_serializer=gateway__pb2.ClientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'openapi.Quote', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Quote(object):
    """The greeting service definition.
    """

    @staticmethod
    def StreamRequest(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/openapi.Quote/StreamRequest',
            gateway__pb2.ClientRequest.SerializeToString,
            gateway__pb2.ClientResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
