from flask_restx import Namespace, Resource, fields
from app.services.driving_service import DrivingService

driving_controller = Namespace('driving', description='driving operations')


driving_model= driving_controller.model('DrivingAppointment',{
        'id': fields.Integer(readonly=True),
        'test_date_driving':fields.Date(required=True,description='Test date driving'),
        'created_at': fields.DateTime(readonly=True),
        'updated_at': fields.DateTime(readonly=True),
})



@driving_controller.route('/')
class DrivingList(Resource):
    @driving_controller.marshal_list_with(driving_model)
    def get(self):
        """List all drivings"""
        return DrivingService.get_all_drivings()

    @driving_controller.expect(driving_model)
    @driving_controller.marshal_with(driving_model, code=201)
    def post(self):
        """Create a new driving appointment"""
        data = driving_controller.payload
        driving = DrivingService.create_driving(data)
        return driving, 201
    


@driving_controller.route('/<int:driving_id>')
@driving_controller.param('driving_id', 'The driving identifier')
class DrivingsDetails(Resource):


    @driving_controller.marshal_list_with(driving_model)
    @driving_controller.response(200, 'Success')
    @driving_controller.response(404, 'Driving not found')
    def get(self,driving_id):
        """Fetch driving by id"""
        return DrivingService.get_driving_by_id(driving_id) 

    @driving_controller.response(200, 'Success')
    @driving_controller.response(404, 'Driving not found')
    def delete(self,driving_id):
        """Delete a specific Driving"""
        return DrivingService.delete_driving_by_id(driving_id)
    
    
    @driving_controller.expect(driving_model)
    @driving_controller.marshal_with(driving_model, code=201)
    def put(self,driving_id):
        """update a driving"""
        driving = DrivingService.update_driving_by_id(driving_id)
        return driving,201

