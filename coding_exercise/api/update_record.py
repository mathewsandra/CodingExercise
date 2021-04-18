from flask_restful import Resource
from flask import request
from flask_restful import abort
from controller.update_record_controller import update_record_controller



updateRecordController = update_record_controller()

class update_record(Resource):

    def patch(self, audioFileType, audioFileID):
        try:
            json_data = request.get_json(force=True)
            data = updateRecordController.detect_file_type(audioFileType, audioFileID, json_data)
            
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data  