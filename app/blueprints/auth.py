from flask import Blueprint, request, jsonify
from app.models import User
from app.extensions import db


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({'message': '请提供json数据'}), 400
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    if not username or not password or not email:
        return jsonify({'message': '缺少用户名或密码或邮箱'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'message': '该用户名已经被占用'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'message': '该邮箱已经被占用'}), 400
    user = User(username=username, email=email)
    user.set_password(password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': username, 'email': email, 'password': password, 'message': '注册成功！'}), 201
