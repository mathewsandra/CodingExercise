from flask_restful import Resource
from flask import request
from flask_restful import abort
from controller.get_data_controller import get_data_controller

getDataController = get_data_controller()

class get_data(Resource):

    def get(self, audioFileType, audioFileID=None):
        try:
            
            data = getDataController.detect_file_type(audioFileType, audioFileID)
           
            
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data  