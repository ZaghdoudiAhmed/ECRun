from ..models.DrivingAppointment import DrivingAppointment
from flask import make_response,jsonify,request
from app.extensions import *



class DrivingService:
    """Driving services"""


    # get all drivings
    def get_all_drivings():
        try:
            drivings = DrivingAppointment.query.all()
            return drivings , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting drivings'}), 500)



    # get driving by id
    def get_driving_by_id(id_driving):
        try:
            driving = DrivingAppointment.query.filter_by(id=id_driving).first()
            if driving:
                return driving,200
            return make_response(jsonify({'message': 'driving not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error getting driving'}), 500)



    # create a driving
    def create_driving(driving_data):
        try:
            driving = DrivingAppointment(driving_data)
            db.session.add(driving)
            db.session.commit()
            
            return driving, 201
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # delete a driving
    def delete_driving_by_id(driving_id):
        try:
            driving = DrivingAppointment.query.filter_by(id=driving_id).first()
            if driving:
                db.session.delete(driving)
                db.session.commit()
                return make_response(jsonify({'message': 'driving deleted'}), 200)
            return make_response(jsonify({'message': 'driving not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # update a driving  
    def update_driving_by_id(driving_id):
        try:
            driving = DrivingAppointment.query.filter_by(id=driving_id).first()
            if driving:
                data = request.get_json()
                db.session.commit()
                return make_response(jsonify({'message': 'driving updated'}), 200)
            return make_response(jsonify({'message': 'driving not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error updating driving'}), 500)
