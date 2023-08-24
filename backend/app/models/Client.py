from app.extensions import db
from sqlalchemy.sql import func


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    phone_number = db.Column(db.Integer)
    cin_number = db.Column(db.Integer, nullable=False)
    cin_recto = db.Column(db.Text, nullable=False)
    cin_verso = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime, default=None, nullable=True)
    date_of_birth = db.Column(db.DateTime(), nullable=False)
    nb_hours_code = db.Column(db.Integer, default=0)
    nb_hours_driving = db.Column(db.Integer, default=0)
    # code_appointments = db.relationship(
    #     'CodeAppointment', cascade='all, delete',  backref=db.backref('Client', lazy=True))
    # driving_appointments = db.relationship(
    #     'DrivingAppointment', cascade='all, delete',  backref=db.backref('Client', lazy=True))
