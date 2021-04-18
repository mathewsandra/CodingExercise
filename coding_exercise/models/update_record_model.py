from schema.all_schemas import audiobook, podcast, song, db
from flask_restful import abort
import datetime 
import calendar

class update_record_model():
    def update_song_record(self, audioFileID, file_metadata):
        try:
            record = db.session.query(song).filter(song.songId == int(audioFileID)).first()
            if record == None:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                if record.status == 0:
                    response = {"status":0, "message":"Cannot update deleted record"}
                else:
                    utc_timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
                    record.songName=file_metadata['songName'].lower()
                    record.seconds = int(file_metadata['seconds'])
                    record.updatedOn = utc_timestamp
                    db.session.commit()
                    db.session.close()
                    response = {"status":200, "message":"OK"}
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response

    def update_audiobook_record(self, audioFileID, file_metadata):
        try:
            record = db.session.query(audiobook).filter(audiobook.audiobookId == int(audioFileID)).first()
            if record == None:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                if record.status == 0:
                    response = {"status":0, "message":"Cannot update deleted record"}
                else:
                    utc_timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
                    record.audiobookTitle=file_metadata['audiobookTitle'].lower()
                    record.author = file_metadata['author'].lower()
                    record.narrator = file_metadata['narrator'].lower()
                    record.seconds = int(file_metadata['seconds'])
                    record.updatedOn = utc_timestamp
                    db.session.commit()
                    db.session.close()
                    response = {"status":200, "message":"OK"}
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response
    
    def update_podcast_record(self, audioFileID, file_metadata):
        try:
            record = db.session.query(podcast).filter(podcast.podcastId == int(audioFileID)).first()
            if record == None:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                if record.status == 0:
                    response = {"status":0, "message":"Cannot update deleted record"}
                else:
                    utc_timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

                    if "participants" not in file_metadata:
                        file_metadata["participants"] = []
                    record.podcastName=file_metadata['podcastName'].lower()
                    record.seconds = int(file_metadata['seconds'])
                    record.host = file_metadata['host'].lower()
                    record.participants = file_metadata['participants']
                    record.updatedOn = utc_timestamp
                    db.session.commit()
                    db.session.close()
                    response = {"status":200, "message":"OK"}
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response
    