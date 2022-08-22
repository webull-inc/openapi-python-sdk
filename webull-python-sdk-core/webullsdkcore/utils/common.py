# coding=utf-8
import base64
import hashlib
import socket
from datetime import datetime
import uuid
import json
from webullsdkcore.compat import ensure_bytes, ensure_string

TIME_ZONE = "UTC"
FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%SZ"
FORMAT_ISO_8601_MILLIS = "%Y-%m-%dT%H:%M:%S.%fZ"

def get_uuid():
    name = socket.gethostname() + str(uuid.uuid1())
    namespace = uuid.NAMESPACE_URL
    return str(uuid.uuid5(namespace, name))

def get_iso_8601_date(dt_as_utc=None):
    if dt_as_utc:
        return dt_as_utc.strftime(FORMAT_ISO_8601)
    d = datetime.utcnow()
    return d.strftime(FORMAT_ISO_8601)

def get_iso_8601_date_with_millis(dt_as_utc=None):
    if dt_as_utc:
        d = dt_as_utc
    else:
        d = datetime.utcnow()
    ret = d.strftime(FORMAT_ISO_8601_MILLIS)
    if len(ret) != 27:
        raise RuntimeError("failed to convent timestamp, result: %s" % ret)
    return ret[:-4] + ret[-1:]

def parse_timestamp_to_dt(timestamp_of_millis):
    return datetime.utcfromtimestamp(timestamp_of_millis / 1000.0)

def md5_sum(content):
    content_bytes = ensure_bytes(content)
    md5_bytes = hashlib.md5(content_bytes).digest()
    return ensure_string(base64.standard_b64encode(md5_bytes))

def md5_hex(content):
    content_bytes = ensure_bytes(content)
    return hashlib.md5(content_bytes).hexdigest()

def json_dumps_compact(content):
    return json.dumps(content, ensure_ascii=False, separators=(',', ':'))