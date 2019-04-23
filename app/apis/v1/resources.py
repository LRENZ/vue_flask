from flask import jsonify, request, g
from flask.views import MethodView
from app.apis.v1 import bp
from app.apis.v1.errors import api_abort
from app.apis.v1.auth import generate_token, auth_required
from app.apis.v1.schemas import user_schema
from app.models import User


class IndexAPI(MethodView):
    def get(self):
        return jsonify({
            'api_version': '1.0',
            'api_root_url': request.url,
            'current_user_url': f'{request.url}user'
        })


class AuthTokenAPI(MethodView):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        user = User.query.filter_by(username=username).first()
        if user is None:
            return api_abort(400, '该用户不存在。')
        elif not user.check_password(password):
            return api_abort(400, '密码错误。')
        token, expiration = generate_token(user)
        response = jsonify({'access_token': token, 'token_type': 'Bearer', 'expires_in': expiration})
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


class UserAPI(MethodView):
    decorators = [auth_required]

    def get(self):
        return jsonify(user_schema(g.current_user))


bp.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])
bp.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('token'), methods=['POST'])
bp.add_url_rule('/user', view_func=UserAPI.as_view('user'), methods=['GET'])
