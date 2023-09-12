from flask_restx import Namespace, Resource, fields
from app.services.quiz_service import QuizService
from app.controllers.question_controller import question_model
from app.models.Quiz import Quiz



quiz_controller = Namespace('quiz', description='quiz operations')


quiz_model = quiz_controller.model('Quiz',{
    'id': fields.Integer(readonly=True),
    'uuid': fields.String(readonly=True),
    'score': fields.Integer(required=True,description= 'Score'),
    'questions':  fields.List(fields.Nested(question_model),readonly=True,description='Liste questions'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True),
})




@quiz_controller.route('/')
class QuizList(Resource):
    @quiz_controller.marshal_list_with(quiz_model)
    def get(self):
        """List all quizs"""
        return QuizService.get_all_quiz()

    @quiz_controller.expect(quiz_model)
    @quiz_controller.marshal_with(quiz_model, code=201)
    def post(self):
        """Create a new quiz"""
        data = quiz_controller.payload
        quiz = QuizService.create_quiz(data)
        return quiz, 201
    


@quiz_controller.route('/<int:quiz_id>')
@quiz_controller.param('quiz_id', 'The quiz identifier')
class QuizsDetails(Resource):


    @quiz_controller.marshal_list_with(quiz_model)
    @quiz_controller.response(200, 'Success')
    @quiz_controller.response(404, 'Quiz not found')
    def get(self,quiz_id):
        """Fetch quiz by id"""
        return QuizService.get_quiz_by_id(quiz_id) 

    @quiz_controller.response(200, 'Success')
    @quiz_controller.response(404, 'Quiz not found')
    def delete(self,quiz_id):
        """Delete a specific Quiz"""
        return QuizService.delete_quiz_by_id(quiz_id)
    
    
    @quiz_controller.expect(quiz_model)
    @quiz_controller.marshal_with(quiz_model, code=201)
    def put(self,quiz_id):
        """update a quiz"""
        quiz = QuizService.update_quiz_by_id(quiz_id)
        return quiz,201

