from ..models.Quiz import Quiz
from flask import make_response,jsonify,request
from app.extensions import *



class QuizService:
    """Quiz services"""



    # get all quizs
    def get_all_quiz():
        try:
            quizs = Quiz.query.all()
            return quizs , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting quizs'}), 500)



    # get quiz by id
    def get_quiz_by_id(id_quiz):
        try:
            quiz = Quiz.query.filter_by(id=id_quiz).first()
            if quiz:
                return quiz,200
            return make_response(jsonify({'message': 'quiz not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error getting quiz'}), 500)



    # create a quiz
    def create_quiz(quiz_data):
        try:
            quiz = Quiz(quiz_data)
            db.session.add(quiz)
            db.session.commit()
            
            return quiz, 201
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # delete a quiz
    def delete_quiz_by_id(quiz_id):
        try:
            quiz = Quiz.query.filter_by(id=quiz_id).first()
            if quiz:
                db.session.delete(quiz)
                db.session.commit()
                return make_response(jsonify({'message': 'quiz deleted'}), 200)
            return make_response(jsonify({'message': 'quiz not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # update a quiz  
    def update_quiz_by_id(quiz_id):
        try:
            quiz = Quiz.query.filter_by(id=quiz_id).first()
            if quiz:
                data = request.get_json()
                db.session.commit()
                return make_response(jsonify({'message': 'quiz updated'}), 200)
            return make_response(jsonify({'message': 'quiz not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error updating quiz'}), 500)
