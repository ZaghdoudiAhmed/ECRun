from app.extensions import db
from sqlalchemy.sql import func


class DrivingAppointment(db.Model):
    __tablename__ = 'driving_appointment'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    test_date_driving = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
