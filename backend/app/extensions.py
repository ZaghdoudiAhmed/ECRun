from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from flask_restx import Api
from flask_cors import CORS

db = SQLAlchemy()
fake = Faker()
api = Api()
cors = CORS()