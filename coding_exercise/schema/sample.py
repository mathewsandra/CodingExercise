from sqlalchemy import Table, Column, Integer, String
from .all_schemas import db

class sample(db.Model):

    __tablename__ = 'sample'
    sample_id = db.Column(db.Integer, primary_key=True)
    sample_description = db.Column(db.String(120), unique=True, nullable=False)