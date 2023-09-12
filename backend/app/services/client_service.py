from ..models.Client import Client
from flask import make_response,jsonify,request
from app.extensions import *

class ClientService:
    """Client services"""



    # get all clients
    def get_all_clients():
        try:
            clients = Client.query.all()
            return clients , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting clients'}), 500)



    # get client by id
    def get_client_by_id(id_client):
        try:
            client = Client.query.filter_by(id=id_client).first()
            if client:
                return client,200
            return make_response(jsonify({'message': 'client not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error getting client'}), 500)



    # create a client
    def create_client(client_data):
        try:
            client = Client(client_data)
            db.session.add(client)
            db.session.commit()
            
            return client, 201
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # delete a client
    def delete_client_by_id(client_id):
        try:
            client = Client.query.filter_by(id=client_id).first()
            if client:
                db.session.delete(client)
                db.session.commit()
                return make_response(jsonify({'message': 'client deleted'}), 200)
            return make_response(jsonify({'message': 'client not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # update a client  
    def update_client_by_id(client_id):
        try:
            client = Client.query.filter_by(id=client_id).first()
            if client:
                data = request.get_json()
                db.session.commit()
                return make_response(jsonify({'message': 'client updated'}), 200)
            return make_response(jsonify({'message': 'client not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error updating client'}), 500)
