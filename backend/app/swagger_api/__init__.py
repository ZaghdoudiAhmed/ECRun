from flask import Blueprint
from flask_restx import Api
from app.controllers.client_controller import client_controller
from app.controllers.quiz_controller import quiz_controller
from app.controllers.question_controller import question_controller
from app.controllers.response_controller import response_controller
from app.controllers.code_controller import code_controller
from app.controllers.driving_controller import driving_controller


api_v1 = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_v1,
          title='EC RUN RESTFULL API',
          version='1.0',
          description='an API for Driving school project',
          )


api.add_namespace(client_controller)
api.add_namespace(quiz_controller)
api.add_namespace(response_controller)
api.add_namespace(question_controller)
api.add_namespace(code_controller)
api.add_namespace(driving_controller)
