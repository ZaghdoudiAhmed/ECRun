from flask_restx import Namespace, Resource, fields
from app.services.response_service import ResponseService
from app.models.Response import Response


response_controller = Namespace('response', description='response operations')


response_model = response_controller.model('Response',{
    'id': fields.Integer(readonly=True),
    'text': fields.String(readonly=True),
    'is_correct': fields.Boolean(required=True,description= 'Response status'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True),
})




@response_controller.route('/')
class ResponseList(Resource):
    @response_controller.marshal_list_with(response_model)
    def get(self):
        """List all responses"""
        return ResponseService.get_all_response()

    @response_controller.expect(response_model)
    @response_controller.marshal_with(response_model, code=201)
    def post(self):
        """Create a new response"""
        data = response_controller.payload
        response = ResponseService.create_response(data)
        return response, 201
    


@response_controller.route('/<int:response_id>')
@response_controller.param('response_id', 'The response identifier')
class ResponsesDetails(Resource):


    @response_controller.marshal_list_with(response_model)
    @response_controller.response(200, 'Success')
    @response_controller.response(404, 'Response not found')
    def get(self,response_id):
        """Fetch response by id"""
        return ResponseService.get_response_by_id(response_id) 

    @response_controller.response(200, 'Success')
    @response_controller.response(404, 'Response not found')
    def delete(self,response_id):
        """Delete a specific Response"""
        return ResponseService.delete_response_by_id(response_id)
    
    
    @response_controller.expect(response_model)
    @response_controller.marshal_with(response_model, code=201)
    def put(self,response_id):
        """update a response"""
        response = ResponseService.update_response_by_id(response_id)
        return response,201

