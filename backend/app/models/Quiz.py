from app.extensions import db
from sqlalchemy.sql import func


class Quiz(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    uuid = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer)
    questions = db.relationship('Question', backref='quiz', lazy=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('code_appointment.id'))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
