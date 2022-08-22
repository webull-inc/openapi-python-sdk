# coding=utf-8
class ClientException(Exception):
    def __init__(self, code, msg=""):
        Exception.__init__(self)
        self.error_code = code
        self.error_msg = msg
        
    def __str__(self):
        return "%s %s" % (self.error_code, self.error_msg)

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg

class ServerException(Exception):
    def __init__(self, code, msg="", http_status = None, request_id = None):
        Exception.__init__(self)
        self.error_code = code
        self.error_msg = msg
        self.http_status = http_status
        self.request_id = request_id

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg

    def get_http_status(self):
        return self.http_status

    def get_request_id(self):
        return self.request_id

    def __str__(self):
        return "HTTP Status: %s, Code: %s, Msg: %s, RequestID: %s" \
    % (str(self.http_status), self.error_code, self.error_msg, self.request_id)