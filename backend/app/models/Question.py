from app.extensions import db
from sqlalchemy.sql import func


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    text = db.Column(db.String(255))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    responses = db.relationship('Response', backref='question', cascade='all, delete-orphan', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
