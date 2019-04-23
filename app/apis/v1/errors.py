from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from app.apis.v1 import bp


def api_abort(code, message=None, **kwargs):
    message = message if message else HTTP_STATUS_CODES.get(code, '')
    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response


def token_missing():
    response = api_abort(401)
    response.headers['WWW-Authenticate'] = 'Bearer'
    return response


def invalid_token():
    response = api_abort(401, 'invalid or expired token.')
    response.headers['WWW-Authenticate'] = 'Bearer'
    return response
