import os
from flask import Flask
from app.config import config
from app.extensions import *
from app.models import User
from app.blueprints.auth import bp as auth_bp
from app.apis.v1 import bp as api_v1_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    from flask import Flask, render_template
    app = Flask(__name__,
                static_folder="../dist/static",
                template_folder="../dist")
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    return app


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User}
