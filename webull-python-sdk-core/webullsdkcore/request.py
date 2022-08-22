# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8
import abc
from webullsdkcore.auth.algorithm import sha_hmac1
from webullsdkcore.vendored.six import iterkeys
from webullsdkcore.vendored.six import iteritems
from webullsdkcore.vendored.six import add_metaclass
from webullsdkcore.http import protocol_type
from webullsdkcore.exception import exceptions, error_code
from webullsdkcore.vendored.requests.structures import CaseInsensitiveDict
from webullsdkcore.vendored.six.moves.urllib.parse import urlencode
from webullsdkcore.auth.composer import default_signature_composer as sc
import webullsdkcore.headers as hd


_default_protocol_type = protocol_type.HTTPS

def set_default_protocol_type(user_protocol_type):
    global _default_protocol_type
    if user_protocol_type == protocol_type.HTTP or user_protocol_type == protocol_type.HTTPS:
        _default_protocol_type = user_protocol_type
    else:
        raise exceptions.ClientException(error_code.SDK_INVALID_PARAMETER)

def get_default_protocol_type():
    return _default_protocol_type

@add_metaclass(abc.ABCMeta)
class BaseRequest:
    def __init__(self, 
                 version=None,
                 action_name=None,
                 accept_format=None,
                 protocol_type=None,
                 method=None):
        """
        :param version:
        :param action_name:
        :param params:
        :param resource_owner_account:
        :param protocol_type:
        :param accept_format:
        :return:
        """
        self._version = version
        self._action_name = action_name
        self._protocol_type = protocol_type
        if self._protocol_type is None:
            self._protocol_type = _default_protocol_type
        self._accept_format = accept_format
        self._params = {}
        self._method = method
        self._header = {}
        if version is not None:
            self.add_header(hd.VERSION, version)
        self._body_params = {}
        self._uri_pattern = None
        self._uri_params = None
        self._content = None
        self._extra_user_agent = {}
        self.string_to_sign = ''
        self._request_connect_timeout = None
        self._request_read_timeout = None
        self.endpoint = None

    def add_query_param(self, k, v):
        self._params[k] = v

    def add_body_params(self, k, v):
        self._body_params[k] = v

    def get_body_params(self):
        return self._body_params

    def get_uri_pattern(self):
        return self._uri_pattern

    def get_uri_params(self):
        return self._uri_params

    def get_version(self):
        return self._version

    def get_action_name(self):
        return self._action_name

    def get_accept_format(self):
        return self._accept_format

    def get_protocol_type(self):
        return self._protocol_type

    def get_query_params(self):
        return self._params

    def get_method(self):
        return self._method

    def set_uri_pattern(self, pattern):
        self._uri_pattern = pattern

    def set_uri_params(self, params):
        self._uri_params = params

    def set_method(self, method):
        self._method = method

    def set_version(self, version):
        self._header[hd.VERSION] = version
        self._version = version

    def set_action_name(self, action_name):
        self._action_name = action_name

    def set_accept_format(self, accept_format):
        self._accept_format = accept_format

    def set_protocol_type(self, protocol_type):
        self._protocol_type = protocol_type

    def set_query_params(self, params):
        self._params = params

    def set_body_params(self, body_params):
        self._body_params = body_params

    def set_content(self, content):
        """
        :param content: ByteArray
        :return:
        """
        self._content = content

    def get_content(self):
        """
        :return: ByteArray
        """
        return self._content

    def get_headers(self):
        """
        :return: Dict
        """
        return self._header

    def set_headers(self, headers):
        """
        :param headers: Dict
        :return:
        """
        self._header = headers

    def add_header(self, k, v):
        self._header[k] = v

    def set_user_agent(self, agent):
        self.add_header(hd.NATIVE_USER_AGENT, agent)

    def append_user_agent(self, key, value):
        self._extra_user_agent.update({key: value})

    def request_user_agent(self):
        request_user_agent = {}
        if hd.NATIVE_USER_AGENT in self.get_headers():
            request_user_agent.update({
                'request': self.get_headers().get(hd.NATIVE_USER_AGENT)
            })
        else:
            request_user_agent.update(self._extra_user_agent)

        return CaseInsensitiveDict(request_user_agent)

    def set_content_type(self, content_type):
        self.add_header(hd.NATIVE_CONTENT_TYPE, content_type)

    @abc.abstractmethod
    def get_signed_header(self, host, app_key, app_secret):
        pass

    def get_connect_timeout(self):
        return self._request_connect_timeout

    def set_connect_timeout(self, connect_timeout):
        self._request_connect_timeout = connect_timeout

    def get_read_timeout(self):
        return self._request_read_timeout

    def set_read_timeout(self, read_timeout):
        self._request_read_timeout = read_timeout

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def get_endpoint(self):
        return self.endpoint
class ApiRequest(BaseRequest):
    def __init__(
        self,
        request_path,
        version=None,
        method='POST',
        headers=None,
        query_params=None,
        body_params=None,
        protocol=None,
        signer_spec=sha_hmac1):
        BaseRequest.__init__(
            self,
            version,
            request_path,
            "JSON",
            protocol,
            method)
        self._method = method
        self._header = headers or {}
        self._params = query_params or {}
        if version is not None:
            self.add_header(hd.VERSION, version)
        self._signer_spec = signer_spec
        self.set_body_params(body_params)

    def get_signed_header(self, host, app_key, app_secret):
        sc.calc_signature(self._header, host, self._action_name, self._params, self._body_params, app_key, app_secret, self._signer_spec)
        return self._header

    def get_url(self):
        """
        Compose request url without domain
        :return: String
        """
        url = self._action_name
        if self._params:
            if not url.endswith("?"):
                url += "?" 
            url += urlencode(self._params)
            if url.endswith("?"):
               url = url[0:(len(url) - 1)] 
        return url