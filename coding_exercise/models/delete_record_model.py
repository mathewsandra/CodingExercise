from schema.all_schemas import audiobook, podcast, song, db
from flask_restful import abort

class delete_record_model():
    def delete_song_record(self, audioFileID):
        try:
            record = db.session.query(song).filter(song.songId == int(audioFileID)).first()
            if record == None:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                if record.status == 0:
                    response = {"status":0, "message":"Record already deleted"}
                else:
                    record.status = 0
                    db.session.commit()
                    db.session.close()
                    response = {"status":200, "message":"OK"}
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response

    def delete_audiobook_record(self, audioFileID):
        try:
            record = db.session.query(audiobook).filter(audiobook.audiobookId == int(audioFileID)).first()
            if record == None:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                if record.status == 0:
                    response = {"status":0, "message":"Record already deleted"}
                else:
                    record.status = 0
                    db.session.commit()
                    db.session.close()
                    response = {"status":200, "message":"OK"}
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response
    
    def delete_podcast_record(self, audioFileID):
        try:
            record = db.session.query(podcast).filter(podcast.podcastId == int(audioFileID)).first()
            if record == None:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                if record.status == 0:
                    response = {"status":0, "message":"Record already deleted"}
                else:
                    record.status = 0
                    db.session.commit()
                    db.session.close()
                    response = {"status":200, "message":"OK"}
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response
    