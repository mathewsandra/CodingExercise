from models.create_record_model import create_record_model
from flask_restful import Resource,abort
from schematics.models import Model
from schematics.types import StringType, ListType, IntType


createRecordModel = create_record_model()

class song_data_validate(Model):
    songName = StringType(required=True)
    seconds = IntType(required=True)
    
class podcast_data_validate(Model):
    podcastName = StringType(required=True)
    seconds = IntType(required=True)
    host = StringType(required=True)
    participants = ListType(StringType, required=False)

class audiobook_data_validate(Model):
	audiobookTitle = StringType(required=True)
	author = StringType(required=True)
	narrator = StringType(required=True)
	seconds = IntType(required=True)

class create_record_controller():

    def detect_file(self, json_data):
        try:
            print("inside *********")
            file_metadata = json_data["audioFileMetadata"]
            if json_data['audioFileType'] == "song":
                validator = song_data_validate(file_metadata)
                validator.validate()
                del validator
                data = createRecordModel.save_song_record(file_metadata)
                
            elif json_data['audioFileType'] == "audiobook":
                validator = audiobook_data_validate(file_metadata)
                validator.validate()
                del validator
                data = createRecordModel.save_audiobook_record(file_metadata)
                
            elif json_data['audioFileType'] == "podcast":
                validator = podcast_data_validate(file_metadata)
                validator.validate()
                del validator
                data = createRecordModel.save_podcast_record(file_metadata)
                          
            else:
                return "Bad Request", 400

            print("hihihi")
            

        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data