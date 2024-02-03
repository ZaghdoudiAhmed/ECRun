from ..models.CodeAppointment import CodeAppointment
from flask import make_response,jsonify,request
from app.extensions import *



class CodeService:
    """Code services"""


    # get all code
    def get_all_cods():
        try:
            cods = CodeAppointment.query.all()
            return cods , 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting cods'}), 500)



    # get code by id
    def get_code_by_id(id_code):
        try:
            code = CodeAppointment.query.filter_by(id=id_code).first()
            if code:
                return code,200
            return make_response(jsonify({'message': 'code not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error getting code'}), 500)



    # create a code
    def create_code(code_data):
        try:
            code = CodeAppointment(code_data)
            db.session.add(code)
            db.session.commit()
            
            return code, 201
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # delete a code
    def delete_code_by_id(code_id):
        try:
            code = CodeAppointment.query.filter_by(id=code_id).first()
            if code:
                db.session.delete(code)
                db.session.commit()
                return make_response(jsonify({'message': 'code deleted'}), 200)
            return make_response(jsonify({'message': 'code not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': e}), 500)


    # update a code  
    def update_code_by_id(code_id):
        try:
            code = CodeAppointment.query.filter_by(id=code_id).first()
            if code:
                data = request.get_json()
                db.session.commit()
                return make_response(jsonify({'message': 'code updated'}), 200)
            return make_response(jsonify({'message': 'code not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'error updating code'}), 500)
