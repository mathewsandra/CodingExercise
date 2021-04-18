from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

# from .sample import sample
from .podcast import podcast
from .audiobook import audiobook
from .song import song