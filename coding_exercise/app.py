from flask import Flask

app = Flask(__name__)

def init():
    import settings
    app.config.from_object(settings)

    from schema.all_schemas import db
    # db.create_all()
    # db.drop_all()

    from api.api_loader import load_api
    load_api(app)

    return app

