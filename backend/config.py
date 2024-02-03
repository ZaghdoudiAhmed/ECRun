"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY') or 'ecole_conduite_run'

    # Configuration Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')\
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
