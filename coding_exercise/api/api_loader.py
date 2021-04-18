
from flask_restful import Api
from .sample_func import sample_func, hello_world
from .create_record import create_record
from .delete_record import delete_record
from .update_record import update_record
from .get_data import get_data

def load_api(app):

    apis = Api(app)
    apis.add_resource(hello_world, '/')
    apis.add_resource(create_record, '/createRecord')
    apis.add_resource(delete_record, '/deleteRecord/<audioFileType>/<audioFileID>')
    apis.add_resource(update_record, '/updateRecord/<audioFileType>/<audioFileID>')
    apis.add_resource(get_data, '/getData/<audioFileType>', '/getData/<audioFileType>/<audioFileID>')




  