from models.delete_record_model import delete_record_model
from flask_restful import abort


deleteRecordModel = delete_record_model()

class delete_record_controller():

    def detect_file_type(self, audioFileType, audioFileID):
        try:

            if audioFileType == "song":
                    
                data = deleteRecordModel.delete_song_record(audioFileID)
                    
            elif audioFileType == "audiobook":
                    
                data = deleteRecordModel.delete_audiobook_record(audioFileID)
                    
            elif audioFileType == "podcast":
                
                data = deleteRecordModel.delete_podcast_record(audioFileID)
                
            else:
                return "Bad Request", 400
        
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data
                          
