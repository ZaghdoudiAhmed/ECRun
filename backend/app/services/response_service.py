from ..models.Response import Response
from flask import make_response,jsonify,request
from app.extensions import *


class ResponseService:
    """Response services"""


    # get all responses 
    def get_all_response():
        try:
            responses = Response.query.all()
            return responses , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting responses'}), 500)



    # get response by id
    def get_response_by_id(id_response):
        try:
            response = Response.query.filter_by(id=id_response).first()
            if response:
                return response,200
            return make_response(jsonify({'message': 'response not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error getting response'}), 500)



    # create a response
    def create_response(response_data):
        try:
            response = Response(response_data)
            db.session.add(response)
            db.session.commit()
            
            return response, 201
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # delete a response
    def delete_response_by_id(response_id):
        try:
            response = Response.query.filter_by(id=response_id).first()
            if response:
                db.session.delete(response)
                db.session.commit()
                return make_response(jsonify({'message': 'response deleted'}), 200)
            return make_response(jsonify({'message': 'response not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # update a response  
    def update_response_by_id(response_id):
        try:
            response = Response.query.filter_by(id=response_id).first()
            if response:
                data = request.get_json()
                db.session.commit()
                return make_response(jsonify({'message': 'response updated'}), 200)
            return make_response(jsonify({'message': 'response not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error updating response'}), 500)


    # Get responses of a specifique question
    def get_responses_of_quiz(question_id):
        try:
            responses = Response.query.filter_by(question_id=question_id).all()
            return responses , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting responses of question'}), 500)

