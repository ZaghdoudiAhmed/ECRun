from ..models.Question import Question
from flask import make_response,jsonify,request
from app.extensions import *



class QuestionService:
    """Question services"""


    # get all questions 
    def get_all_question():
        try:
            questions = Question.query.all()
            return questions , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting questions'}), 500)



    # get question by id
    def get_question_by_id(id_question):
        try:
            question = Question.query.filter_by(id=id_question).first()
            if question:
                return question,200
            return make_response(jsonify({'message': 'question not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error getting question'}), 500)



    # create a question
    def create_question(question_data):
        try:
            question = Question(question_data)
            db.session.add(question)
            db.session.commit()
            
            return question, 201
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # delete a question
    def delete_question_by_id(question_id):
        try:
            question = Question.query.filter_by(id=question_id).first()
            if question:
                db.session.delete(question)
                db.session.commit()
                return make_response(jsonify({'message': 'question deleted'}), 200)
            return make_response(jsonify({'message': 'question not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # update a question  
    def update_question_by_id(question_id):
        try:
            question = Question.query.filter_by(id=question_id).first()
            if question:
                data = request.get_json()
                db.session.commit()
                return make_response(jsonify({'message': 'question updated'}), 200)
            return make_response(jsonify({'message': 'question not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error updating question'}), 500)


    # Get questions of a specifique quiz
    def get_questions_of_quiz(quiz_id):
        try:
            questions = Question.query.filter_by(quiz_id=quiz_id).all()
            return questions , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting questions of quiz'}), 500)

