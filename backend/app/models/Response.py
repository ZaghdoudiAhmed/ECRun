from app.extensions import db
from sqlalchemy.sql import func


class Response(db.Model):
    __tablename__ = 'response'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    is_correct = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id'), nullable=False)
