from models.update_record_model import update_record_model
from flask_restful import abort
from schematics.models import Model
from schematics.types import StringType, ListType, IntType


updateRecordModel = update_record_model()

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

class update_record_controller():

    def detect_file_type(self, audioFileType, audioFileID, json_data):
        try:

            if audioFileType == "song":
                validator = song_data_validate(json_data)
                validator.validate()
                del validator    
                data = updateRecordModel.update_song_record(audioFileID, json_data)
                    
            elif audioFileType == "audiobook":
                validator = audiobook_data_validate(json_data)
                validator.validate()
                del validator
                data = updateRecordModel.update_audiobook_record(audioFileID, json_data)
                    
            elif audioFileType == "podcast":
                validator = podcast_data_validate(json_data)
                validator.validate()
                del validator
                data = updateRecordModel.update_podcast_record(audioFileID, json_data)
            else:
                return "Bad Request", 400
        
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data
                          
