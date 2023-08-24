"""Flask configuration."""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ecole_conduite_run'

    # Configuration Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'postgresql://ECRun:!ChangeMe!@localhost:5432/ECRun'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    DEBUG = False
    TESTING = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
