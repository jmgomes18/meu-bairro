from flask import jsonify
from flask import request


class HttpRequest:
    def __init__(self, headers=None, body=None, params=None):
        self.headers = headers or {}
        self.body = body or {}
        self.params = params or {}


class HttpResponse:
    def __init__(self, data=None, status_code=200, headers=None):
        self.data = data or {}
        self.status_code = status_code
        self.headers = headers or {}


class HttpAdapter:
    @staticmethod
    def get_request_data():
        return HttpRequest(
            headers=request.headers, body=request.get_json(), params=request.args
        )

    @staticmethod
    def make_response(http_response):
        return (
            jsonify(http_response.data),
            http_response.status_code,
            http_response.headers,
        )
