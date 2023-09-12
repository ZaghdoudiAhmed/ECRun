from flask_restx import Namespace, Resource, fields
from app.services.code_service import CodeService
from app.controllers.quiz_controller import quiz_model
code_controller = Namespace('code', description='Code operations')


code_model= code_controller.model('CodeAppointment',{
        'id': fields.Integer(readonly=True),
        'test_date_code':fields.Date(required=True,description='Test date code'),
        'quiz': fields.Nested(quiz_model),
        'created_at': fields.DateTime(readonly=True),
        'updated_at': fields.DateTime(readonly=True),
})



@code_controller.route('/')
class CodeList(Resource):
    @code_controller.marshal_list_with(code_model)
    def get(self):
        """List all cods"""
        return CodeService.get_all_cods()

    @code_controller.expect(code_model)
    @code_controller.marshal_with(code_model, code=201)
    def post(self):
        """Create a new code appointment"""
        data = code_controller.payload
        code = CodeService.create_code(data)
        return code, 201
    


@code_controller.route('/<int:code_id>')
@code_controller.param('code_id', 'The code identifier')
class CodsDetails(Resource):


    @code_controller.marshal_list_with(code_model)
    @code_controller.response(200, 'Success')
    @code_controller.response(404, 'Code not found')
    def get(self,code_id):
        """Fetch code by id"""
        return CodeService.get_code_by_id(code_id) 

    @code_controller.response(200, 'Success')
    @code_controller.response(404, 'Code not found')
    def delete(self,code_id):
        """Delete a specific Code"""
        return CodeService.delete_code_by_id(code_id)
    
    
    @code_controller.expect(code_model)
    @code_controller.marshal_with(code_model, code=201)
    def put(self,code_id):
        """update a code"""
        code = CodeService.update_code_by_id(code_id)
        return code,201

