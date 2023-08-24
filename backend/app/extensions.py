from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from flask_restx import Api

db = SQLAlchemy()
faker = Faker()
api = Api()