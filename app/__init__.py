from flask import Flask
from instance.config import app_config


def create_app(config_name='development'):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024

    from app.api.v1 import blueprint_v1  # noqa

    app.register_blueprint(blueprint_v1, url_prefix='/api/v1/')

    return app
