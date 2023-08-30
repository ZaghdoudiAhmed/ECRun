from app.extensions import db
from app.models.Client import Client
from app.models.CodeAppointment import CodeAppointment
from app.models.DrivingAppointment import DrivingAppointment
from app.models.Quiz import Quiz
from app.models.Question import Question
from app.models.Response import Response
from main import create_app


# File to initialise the database drop all tables and create theme 

app  = create_app() # app instance

with app.app_context():
    db.drop_all() # drop all tables 
    db.create_all() #create all tables 