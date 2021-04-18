from config.config import dialect, username, password, host, database

SQLALCHEMY_DATABASE_URI = str(dialect)+str(username)+":"+str(password)+str(host)+"/"+str(database)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True