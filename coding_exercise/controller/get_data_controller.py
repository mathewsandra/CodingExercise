from models.get_data_model import get_data_model
from flask_restful import abort


getDataModel = get_data_model()

class get_data_controller():

    def detect_file_type(self, audioFileType, audioFileID):
        try:

            if audioFileType == "song":
                    
                data = getDataModel.get_song_data(audioFileID)
                    
            elif audioFileType == "audiobook":
                    
                data = getDataModel.get_audiobook_data(audioFileID)
                    
            elif audioFileType == "podcast":
                
                data = getDataModel.get_podcast_data(audioFileID)
            else:
                return "Bad Request", 400
        
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data
                          
