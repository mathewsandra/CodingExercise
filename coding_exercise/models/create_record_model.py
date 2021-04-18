from schema.all_schemas import audiobook, podcast, song, db
from flask_restful import abort
import datetime 
import calendar
from sqlalchemy import *

class create_record_model():
    def save_song_record(self, file_metadata):
        try:
            utc_timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
          
            record = db.session.query(song).filter(song.songName == file_metadata['songName'].lower()).first()
            if record == None:
                new_record = song(songName=file_metadata['songName'].lower(), seconds = int(file_metadata['seconds']), createdOn = utc_timestamp, updatedOn = utc_timestamp)
                db.session.add(new_record)
                db.session.commit()
                db.session.close()
                finaldata = {"status":1, "message":"Record created successfully"}

            else:
                finaldata = {"status":0, "message":"Record already exists"}

        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return finaldata

    
    def save_audiobook_record(self, file_metadata):
        try:
            utc_timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
        
            record = db.session.query(audiobook).filter(and_(audiobook.audiobookTitle == file_metadata['audiobookTitle'].lower(), audiobook.author == file_metadata['author'].lower(), audiobook.narrator == file_metadata['narrator'].lower())).first() 

            if record == None:
                new_record = audiobook(audiobookTitle=file_metadata['audiobookTitle'].lower(), author = file_metadata['author'].lower(), narrator = file_metadata['narrator'].lower(), seconds = int(file_metadata['seconds']), createdOn = utc_timestamp, updatedOn = utc_timestamp)
                db.session.add(new_record)
                db.session.commit()
                db.session.close()
                finaldata = {"status":1, "message":"Record created successfully"}

            else:
                finaldata = {"status":0, "message":"Record already exists"}

        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return finaldata

    def save_podcast_record(self, file_metadata):
        try:
            utc_timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
            record = db.session.query(podcast).filter(and_(podcast.podcastName == file_metadata['podcastName'].lower(), podcast.host == file_metadata['host'].lower())).first() 

            if record == None:
                if "participants" not in file_metadata:
                    file_metadata["participants"] = []
                new_record = podcast(podcastName=file_metadata['podcastName'].lower(), seconds = int(file_metadata['seconds']), host = file_metadata['host'].lower(), participants = file_metadata['participants'], createdOn = utc_timestamp, updatedOn = utc_timestamp)
                db.session.add(new_record)
                db.session.commit()
                db.session.close()
                finaldata = {"status":1, "message":"Record created successfully"}

            else:
                finaldata = {"status":0, "message":"Record already exists"}


            
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return finaldata