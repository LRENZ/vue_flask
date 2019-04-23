from flask import url_for


def user_schema(user):
    return {
        'id': user.id,
        'self': url_for('.user', external=True),
        'kind': 'User',
        'username': user.username,
        'email': user.email
    }