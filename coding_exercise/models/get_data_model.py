from schema.all_schemas import audiobook, podcast, song, db
from flask_restful import abort
import datetime 
import calendar
from sqlalchemy import *

class get_data_model():
    def get_song_data(self, audioFileID):
        try:
            if audioFileID == None:
                records = db.session.query(song).filter(song.status == 1).all()
            else:
                records = db.session.query(song).filter(and_(song.songId == audioFileID, song.status == 1)).all()

            if records == []:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                data = []
                single_record = {}
                for record in records:
                    single_record["songId"] = record.songId
                    single_record["songName"] = record.songName
                    single_record["seconds"] = record.seconds
                    single_record["createdOn"] = record.createdOn
                    single_record["updatedOn"] = record.updatedOn
                    data.append(single_record.copy())
                    single_record.clear()

                response = {"status":200, "message":"OK", "data": data}

        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response

    
    def get_audiobook_data(self, audioFileID):
        try:
            if audioFileID == None:
                records = db.session.query(audiobook).filter(audiobook.status == 1).all()
            else:
                records = db.session.query(audiobook).filter(and_(audiobook.audiobookId == audioFileID, audiobook.status == 1)).all()
            if records == []:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                data = []
                single_record = {}
                for record in records:
                    single_record["audiobookId"] = record.audiobookId
                    single_record["audiobookTitle"] = record.audiobookTitle
                    single_record["author"] = record.author
                    single_record["narrator"] = record.narrator
                    single_record["seconds"] = record.seconds
                    single_record["createdOn"] = record.createdOn
                    single_record["updatedOn"] = record.updatedOn
                    data.append(single_record.copy())
                    single_record.clear()

                response = {"status":200, "message":"OK", "data": data}

        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response


    def get_podcast_data(self, audioFileID):
        try:
            if audioFileID == None:
                records = db.session.query(podcast).filter(podcast.status == 1).all()
            else:
                records = db.session.query(podcast).filter(and_(podcast.podcastId == audioFileID, podcast.status == 1)).all()
            
            if records == []:
                response = {"status":0, "message":"Record doesnot exists"}
            else:
                data = []
                single_record = {}
                for record in records:
                    single_record["podcastId"] = record.podcastId
                    single_record["podcastName"] = record.podcastName
                    single_record["seconds"] = record.seconds
                    single_record["host"] = record.host
                    single_record["participants"] = record.participants
                    single_record["createdOn"] = record.createdOn
                    single_record["updatedOn"] = record.updatedOn
                    data.append(single_record.copy())
                    single_record.clear()

                response = {"status":200, "message":"OK", "data": data}

        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')
        return response
