from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.schema import CheckConstraint
from .all_schemas import db

class song(db.Model):
    __tablename__ = 'song'
    songId = db.Column(db.Integer, primary_key=True)
    songName = db.Column(db.String(100), nullable=False)
    seconds = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    createdOn = db.Column(db.Integer, nullable=False)
    updatedOn = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        CheckConstraint(seconds >= 0, name='check_song_seconds_positive'),
        {})