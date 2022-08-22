# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8
from asyncio.log import logger
from webullsdkcore.auth.algorithm import sha_hmac1
from webullsdkcore.auth.composer import default_signature_composer
import webullsdkcore.headers as hd
import webullsdkcore.utils.common as core_common
import logging
logger = logging.getLogger(__name__)

def _build_sign_metadata(app_key_id, signer_spec=sha_hmac1):
    sign_params = {}
    sign_algorithm = signer_spec.get_signer_name()
    sign_version = signer_spec.get_signer_version()
    nonce = core_common.get_uuid()
    ts = core_common.get_iso_8601_date() 
    metadata = [
        (hd.APP_KEY, app_key_id),
        (hd.SIGN_ALGORITHM, sign_algorithm),
        (hd.SIGN_VERSION, sign_version),
        (hd.NONCE, nonce),
        (hd.TIMESTAMP, ts)
    ]
    sign_params[hd.APP_KEY] = app_key_id
    sign_params[hd.SIGN_ALGORITHM] = sign_algorithm
    sign_params[hd.SIGN_VERSION] = sign_version
    sign_params[hd.NONCE] = nonce
    sign_params[hd.TIMESTAMP] = ts
    return metadata, sign_params

def _get_body_string(pb_object):
    if pb_object:
        pb_object_bytes = pb_object.SerializeToString()
        return core_common.md5_hex(pb_object_bytes)
    return None
    
def calc_signature(app_key_id, app_key_secret, pb_object, signer_spec=sha_hmac1):
    metadata, sign_params = _build_sign_metadata(app_key_id, signer_spec)
    sign_params = default_signature_composer._lower_key_dict(sign_params)
    logger.debug("sign_params:%s", sign_params)
    body_string = _get_body_string(pb_object)
    logger.debug("body_string:%s" % body_string) 
    string_to_sign = default_signature_composer._build_sign_string(sign_params, None, body_string)
    logger.debug("string_to_sign:%s" % string_to_sign)
    signature = default_signature_composer._gen_signature(string_to_sign, app_key_secret, signer_spec)
    metadata.append((hd.SIGNATURE, signature))
    logger.debug("signature:%s", signature)
    return signature, metadata