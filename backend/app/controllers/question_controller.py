
from flask_restx import Namespace, Resource, fields
from app.services.question_service import QuestionService
from app.models.Question import Question
from app.controllers.response_controller import response_model

question_controller = Namespace('question', description='question operations')


question_model = question_controller.model('Question',{
    'id': fields.Integer(readonly=True),
    'text': fields.String(required=True,description= 'text question'),
    'responses':  fields.List(fields.Nested(response_model),readonly=True,description='Liste reponses'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True),
})


@question_controller.route('/')
class QuestionList(Resource):
    @question_controller.marshal_list_with(question_model)
    def get(self):
        """List all questions"""
        return QuestionService.get_all_question()

    @question_controller.expect(question_model)
    @question_controller.marshal_with(question_model, code=201)
    def post(self):
        """Create a new question"""
        data = question_controller.payload
        question = QuestionService.create_question(data)
        return question, 201
    


@question_controller.route('/<int:question_id>')
@question_controller.param('question_id', 'The question identifier')
class QuestionsDetails(Resource):


    @question_controller.marshal_list_with(question_model)
    @question_controller.response(200, 'Success')
    @question_controller.response(404, 'Question not found')
    def get(self,question_id):
        """Fetch question by id"""
        return QuestionService.get_question_by_id(question_id) 

    @question_controller.response(200, 'Success')
    @question_controller.response(404, 'Question not found')
    def delete(self,question_id):
        """Delete a specific Question"""
        return QuestionService.delete_question_by_id(question_id)
    
    
    @question_controller.expect(question_model)
    @question_controller.marshal_with(question_model, code=201)
    def put(self,question_id):
        """update a question"""
        question = QuestionService.update_question_by_id(question_id)
        return question,201
