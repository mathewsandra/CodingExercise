from flask_restful import Resource
from flask import request
from flask_restful import abort
from schematics.models import Model
from schematics.types import StringType, DictType, UnionType, ListType, NumberType, IntType
from controller.delete_record_controller import delete_record_controller



deleteRecordController = delete_record_controller()

class delete_record(Resource):

    def delete(self, audioFileType, audioFileID):
        try:
            
            data = deleteRecordController.detect_file_type(audioFileType, audioFileID)
            
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data  
