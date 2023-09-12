from app.extensions import db
from sqlalchemy.sql import func


class Response(db.Model):
    __tablename__ = 'response'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    text = db.Column(db.String(255))
    is_correct = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

