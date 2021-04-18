from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.schema import CheckConstraint
from .all_schemas import db

class audiobook(db.Model):
    __tablename__ = 'audiobook'
    audiobookId = db.Column(db.Integer, primary_key=True)
    audiobookTitle = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    seconds = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    createdOn = db.Column(db.Integer, nullable=False)
    updatedOn = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        CheckConstraint(seconds >= 0, name='check_audiobook_seconds_positive'),
        {})