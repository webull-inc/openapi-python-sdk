# coding=utf-8
from webullsdkcore.auth.algorithm import sha_hmac1
from webullsdkcore.exception import error_code
from webullsdkcore.exception.exceptions import ClientException
from webullsdkcore.utils import common
import webullsdkcore.headers as hd
from webullsdkcore.vendored.six import iteritems
from webullsdkcore.vendored.six.moves.urllib.parse import quote
import logging
logger = logging.getLogger(__name__) 

PARAM_KV_JOIN = "="
PARAMS_JOIN = "&"
SECRET_TAILER = "&"

def _refresh_sign_headers(host, headers, app_key_id, signer_spec=sha_hmac1):
    if not host:
        raise ClientException(error_code.SDK_INVALID_PARAMETER)
    sign_headers = {}
    sign_headers[hd.APP_KEY] = app_key_id
    sign_headers[hd.TIMESTAMP] = common.get_iso_8601_date()
    sign_headers[hd.SIGN_VERSION] = signer_spec.get_signer_version()
    sign_headers[hd.SIGN_ALGORITHM] = signer_spec.get_signer_name()
    sign_headers[hd.NONCE] = common.get_uuid()
    headers.update(sign_headers)
    # DO NOT PUT Host Header in headers object, just put into sign_headers
    sign_headers[hd.NATIVE_HOST] = host
    return sign_headers

def _gen_signature(string_to_sign, secret, signer_spec=sha_hmac1):
    return signer_spec.get_sign_string(string_to_sign, secret + SECRET_TAILER)

def _get_body_string(body_params):
    if body_params is not None:
        raw_str = common.json_dumps_compact(body_params)
        hex_digest = common.md5_hex(raw_str)
        return hex_digest.upper()
    else:
        return None

def _build_sign_string(sign_params, uri, body_string):
    string_to_sign = ""
    if uri:
        string_to_sign = uri
    sorted_map = sorted(iteritems(sign_params), key=lambda item: item[0])
    sorted_array = []
    for (k, v) in sorted_map:
        sorted_array.append(str(k) + PARAM_KV_JOIN + v)
    if string_to_sign:
        string_to_sign = string_to_sign + PARAMS_JOIN + PARAMS_JOIN.join(sorted_array)
    else:
        string_to_sign = PARAM_KV_JOIN.join(sorted_array)
    if body_string:
        string_to_sign = string_to_sign + PARAMS_JOIN + body_string
    # All characters except alphabetic characters, digits, -, ., _, ~ will be encoded as %XX.
    # So remove the default safe char '/' which should be quoted as %20F
    return quote(string_to_sign, safe='')

def _lower_key_dict(od):
    lower_key_dict = {}
    for (k, v) in iteritems(od):
        lower_key_dict[k.lower()] = v
    return lower_key_dict

def calc_signature(headers, host, uri, queries, body_params, app_key_id, app_key_secret, signer_spec=sha_hmac1):
    sign_headers = _refresh_sign_headers(host, headers, app_key_id, signer_spec)
    logger.debug("sign_headers:%s", sign_headers)
    sign_params = _lower_key_dict(sign_headers)
    logger.debug("sign_queries:%s", queries)
    if queries :
        for (k, v) in iteritems(queries):
            cv = sign_params.get(k)
            if cv is not None:
                cv = str(cv) + PARAMS_JOIN + str(v)
            else:
                cv = str(v)
            sign_params[k] = cv
    logger.debug("body:%s", body_params)
    body_string = _get_body_string(body_params)
    logger.debug("body_string:%s" % body_string)
    string_to_sign = _build_sign_string(sign_params, uri, body_string)
    logger.debug("string_to_sign:%s" % string_to_sign)
    signature = _gen_signature(string_to_sign, app_key_secret, signer_spec)
    headers[hd.SIGNATURE] = signature
    logger.debug("signature:%s", signature)
    return signature

