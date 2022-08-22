# Copyright 1999-2015 Alibaba Group Holding Ltd.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8

import os
from webullsdkcore.auth import credentials
from webullsdkcore.auth.signers import app_key_signer
from webullsdkcore.exception import exceptions, error_code

class SignerFactory(object):
    @staticmethod
    def get_signer(credential):
        if credential.get('app_key') is not None and credential.get('app_secret') is not None:
            ak_cred = credentials.AppKeyCredential(credential.get('app_key'), credential.get('app_secret'))
            return app_key_signer.AppKeySigner(ak_cred)
        elif os.environ.get('WEBULL_APP_KEY_ID') is not None \
            and os.environ.get('WEBULL_APP_KEY_SECRET') is not None:
                ak_cred = credentials.AppKeyCredential(os.environ.get('WEBULL_APP_KEY_ID'), os.environ.get('WEBULL_APP_KEY_SECRET'))
                return app_key_signer.AppKeySigner(ak_cred)
        else:
            raise exceptions.ClientException(error_code.SDK_INVALID_CREDENTIAL)