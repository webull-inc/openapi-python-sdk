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
from asyncio.log import logger
from webullsdkcore.auth.algorithm import sha_hmac1
from webullsdkcore.auth.composer import default_signature_composer
import webullsdkcore.headers as hd
import webullsdkcore.utils.common as core_common
import logging

from webullsdkcore.headers import WB_USER_ID

logger = logging.getLogger(__name__)


def _build_sign_metadata(app_key_id, host, signer_spec=sha_hmac1, user_id=None):
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

    # If user ID is provided, add it to metadata
    if user_id:
        logger.debug(f"[UserID] add user ID to metadata: {user_id}")
        metadata.append((WB_USER_ID, user_id))
    else:
        logger.debug("[UserID] user ID not provided, no related metadata")

    sign_params[hd.NATIVE_HOST] = host
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


def calc_signature(app_key_id, app_key_secret, host, uri, pb_object, signer_spec=sha_hmac1, user_id=None):
    metadata, sign_params = _build_sign_metadata(app_key_id, host, signer_spec, user_id)
    sign_params = default_signature_composer._lower_key_dict(sign_params)

    body_string = _get_body_string(pb_object)
    string_to_sign = default_signature_composer._build_sign_string(sign_params, uri,
                                                                   body_string)
    signature = default_signature_composer._gen_signature(string_to_sign, app_key_secret, signer_spec)
    metadata.append((hd.SIGNATURE, signature))

    # Check and log whether user ID is included in final metadata
    has_user_id = False
    for key, value in metadata:
        if key == WB_USER_ID:
            has_user_id = True
            logger.debug(f"[UserID] final metadata contains user ID: {value}")
            break

    if not has_user_id and user_id:
        logger.warning(f"[UserID] warning: user ID {user_id} provided but not added to final metadata")

    return signature, metadata


def add_user_id_metadata(metadata, user_id):
    if not user_id:
        return metadata

    # Check if user ID already exists in metadata
    for i, (key, value) in enumerate(metadata):
        if key == WB_USER_ID:
            # Update existing user ID
            logger.debug(f"[UserID] updating existing user ID, from {value} to {user_id}")
            metadata[i] = (WB_USER_ID, user_id)
            return metadata

    # Add new user ID
    logger.debug(f"[UserID] adding new user ID: {user_id}")
    metadata.append((WB_USER_ID, user_id))
    return metadata
