from functools import wraps
from flask import current_app, request, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.apis.v1.errors import api_abort, token_missing, invalid_token
from app.models import User


def generate_token(user):
    expiration = 3600
    serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = serializer.dumps({'id': user.id}).decode('ascii')
    return token, expiration


def get_token():
    if 'Authorization' in request.headers:
        try:
            token_type, token = request.headers['Authorization'].split(None, 1)
        except ValueError:
            token_type = token = None
    else:
        token_type = token = None
    return token_type, token


def validate_token(token):
    serializer = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = serializer.loads(token)
    except (BadSignature, SignatureExpired):
        return False
    user = User.query.get(data['id'])
    if user is None:
        return False
    g.current_user = user
    return True


def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token_type, token = get_token()
        if request.method != 'OPTIONS':
            if token is None:
                return token_missing()
            if not validate_token(token):
                return invalid_token()
            if token_type is None or token_type.lower() != 'bearer':
                return api_abort(400, 'token_type必须是bearer')
        return f(*args, **kwargs)
    return wrapper
