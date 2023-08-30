from flask import Flask,jsonify
from app.extensions import db,api
from config import Config
from flask_migrate import Migrate
from flask_restx import Resource




def create_app(config_class=Config):

    app = Flask(__name__)


    app.config.from_object(Config)
    db.init_app(app)
    api.init_app(app, version='1.0',title='ECRUN API',description='A sample API')
    migrate = Migrate(app, db)


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

    return app
