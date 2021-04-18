from flask_restful import Resource, abort
from flask import request
from schematics.models import Model
from schematics.types import StringType, DictType, UnionType, ListType, NumberType, IntType
from controller.create_record_controller import create_record_controller



createRecordController = create_record_controller()

class json_validate(Model):
    audioFileType = StringType(required=True)
    audioFileMetadata = DictType(UnionType([StringType, IntType, ListType(StringType)]), required=True)


class create_record(Resource):

    def post(self):
        try:
            json_data = request.get_json(force=True)
            print(json_data)
            print(type(json_data))
            validator = json_validate(json_data)
            validator.validate()
            del validator
            data = createRecordController.detect_file(json_data)
            
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data  

