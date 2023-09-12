from flask import Flask
from app.extensions import *
from flask_cors import CORS 
from .swagger_api import api_v1
from flask_migrate import Migrate


def create_app(env=None):
    """This is the initialization function."""
    app = Flask(__name__)

    # if not env:
    #     env = app.config['ENV']

    if env == "development":
        app.config.from_object("config.DevConfig")
    elif env == "testing":
        app.config.from_object("config.TestConfig")
    else:
        app.config.from_object("config.ProdConfig")

    CORS(app,resources={r"/*": {"origins": "*"}})
    # Initialize Flask extensions here

    db.init_app(app)
    cors.init_app(app)
    migrate = Migrate(app, db)

    # jwt.init_app(app)
    # ma.init_app(app)
    # flask_uuid.init_app(app)
    # mail.init_app(app)


    app.register_blueprint(api_v1)
    return app