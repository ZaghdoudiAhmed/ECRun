from flask_restx import Namespace, Resource, fields
from app.services.client_service import ClientService
from app.models.Client import Client
from app.controllers.code_controller import code_model
from app.controllers.driving_controller import driving_model


client_controller = Namespace('client', description='Client operations')

client_model = client_controller.model('Client', {
    'id': fields.Integer(readonly=True),
    'first_name': fields.String(required=True,description= 'FirstName'),
    'last_name' : fields.String(required=True,description= 'LastName'),
    'email': fields.String(required=True,description='Email'),
    'phone_number': fields.Integer(required=True,description='PhoneNumber'),
    'cin_number': fields.Integer(required=True,description='CinNumber'),
    'address': fields.String(required=True,description='Address'),
    'date_of_birth': fields.Date(required=True,description='DateBirth'),
    'nb_hours_code': fields.Integer(required=True,description='NumberHoursCode'),
    'nb_hours_driving': fields.Integer(required=True,description='NumberHoursDriving'),
    'code_appointments': fields.List(fields.Nested(code_model),readonly=True,description='Liste code appointments'),
    'driving_appointments': fields.List(fields.Nested(driving_model),readonly=True,description='Liste driving appointments'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True),
})


@client_controller.route('/')
class ClientList(Resource):
    @client_controller.marshal_list_with(client_model)
    def get(self):
        """List all clients"""
        return ClientService.get_all_clients()

    @client_controller.expect(client_model)
    @client_controller.marshal_with(client_model, code=201)
    def post(self):
        """Create a new client"""
        data = client_controller.payload
        client = ClientService.create_client(data)
        return client, 201
    


@client_controller.route('/<int:client_id>')
@client_controller.param('client_id', 'The client identifier')
class ClientsDetails(Resource):


    @client_controller.marshal_list_with(client_model)
    @client_controller.response(200, 'Success')
    @client_controller.response(404, 'Client not found')
    def get(self,client_id):
        """Fetch client by id"""
        return ClientService.get_client_by_id(client_id) 

    @client_controller.response(200, 'Success')
    @client_controller.response(404, 'Client not found')
    def delete(self,client_id):
        """Delete a specific Client"""
        return ClientService.delete_client_by_id(client_id)
    
    
    @client_controller.expect(client_model)
    @client_controller.marshal_with(client_model, code=201)
    def put(self,client_id):
        """update a client"""
        client = ClientService.update_client_by_id(client_id)
        return client,201

