from flask import Flask,jsonify
from app.extensions import db,faker,api
from config import Config
from flask_migrate import Migrate
from app.models.Client import Client
from app.models.CodeAppointment import CodeAppointment
from app.models.DrivingAppointment import DrivingAppointment
from flask_restx import Resource
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api.init_app(app, version='1.0',title='ECRUN API',description='A sample API')
migrate = Migrate(app, db)


@app.route('/generate_fake_data')
def generate_fake_data():

    # print(faker.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d-%m-%Y')) # birthday
    # print (faker.name()) # first_name + last_name
    # print (faker.email()) # email
    # print (faker.boolean()) 
    # print(faker.address())  # address
    # print (faker.random_int(min= 10000000, max = 99999999)) # CIN
    # print(faker.phone_number()) # phone number
    # print (faker.random_int(min=1, max= 99)) # number hours code + driving
    # for _ in range(10):
    #     client= Client(
    #         first_name= faker.name(),
    #         last_name= faker.name(),
    #         email= faker.email(),
    #         phone_number= faker.random_int(min= 10000000, max = 99999999),
    #         cin_number= faker.random_int(min= 10000000, max = 99999999),
    #         cin_recto= faker.text(),
    #         cin_verso= faker.text(),
    #         address= faker.address(),
    #         date_of_birth=faker.date_of_birth(minimum_age=18, maximum_age=65),
    #     )
    #     db.session.add(client)
    # for _ in range(10):
    #         codeappointment= CodeAppointment(
    #         test_date_code=faker.date_of_birth(minimum_age=18, maximum_age=65),
    #         client_id= faker.random_int(min=35, max = 55)
    #         )
    #         db.session.add(codeappointment)

    for _ in range(10):
            drivingappointment= DrivingAppointment(
            test_date_driving=faker.date_of_birth(minimum_age=18, maximum_age=65),
            client_id= faker.random_int(min=35, max = 55)
            )
            db.session.add(drivingappointment)         
    db.session.commit()
    return 'Base de données peuplée avec succès !'


@api.route('/my-resource/<id>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)

@app.route('/')
def hello():
    return f"Hello, Flask zzz"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
