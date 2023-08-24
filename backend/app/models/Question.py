from app.extensions import db
from sqlalchemy.sql import func


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    responses = db.relationship(
        'Response', cascade='all, delete',  backref=db.backref('Question', lazy=True))
