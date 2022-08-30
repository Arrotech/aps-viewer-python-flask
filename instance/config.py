import os
from os import path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__name__))
load_dotenv(path.join(base_dir, '.env'))


class Config(object):

    """App default settings."""

    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = os.environ.get('DEBUG', False)
    TESTING = os.environ.get('TESTING', False)
    SECRET_KEY = os.environ.get('SECRET_KEY', "secret")
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024 # 500MB


class DevelopmentConfig(Config):

    """Development app settings."""

    DEBUG = True


class ProductionConfig(Config):

    """Production app settings."""

    DEBUG = False
    TESTING = False


class TestingConfig(Config):

    """Testing app configurations."""

    TESTING = True
    DEBUG = True


class ReleaseConfig(Config):

    """Release app configuration settings."""


class StagingConfig(Config):

    """Staging area configuration settings."""

    DEBUG = True


app_config = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestingConfig,
    release=ReleaseConfig,
    staging=StagingConfig
)
