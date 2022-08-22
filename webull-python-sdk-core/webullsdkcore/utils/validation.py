# coding=utf-8

from webullsdkcore.exception.exceptions import ClientException
from webullsdkcore.exception import error_code

def assert_integer_positive(integer, name):
    if isinstance(integer, int) and integer > 0:
        return
    raise ClientException(error_code.SDK_INVALID_PARAMETER,
                          "{0} should be a positive integer.".format(name))