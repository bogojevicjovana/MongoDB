import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymongo


client = pymongo.MongoClient()
db = client.spotify_musicdata
spotify_musicdata = db.artists

track_f = pd.read_csv("D:/Tina/faks/SBP/tracks_features.csv", low_memory = False)
artists_f = pd.read_csv("D:/Tina/faks/SBP/artists.csv",low_memory = False )

#spajanje skupova podataka na osnovu kolone artists

track_f['artists'] = track_f['artists'].str.replace(']', '')
track_f['artists'] = track_f['artists'].str.replace('[', '')
track_f['artists'] = track_f['artists'].str.replace("'", '')

artists_f = artists_f.rename(columns={'artist_mb': 'artists'})
tracks_new = pd.merge(track_f, artists_f, on = 'artists')

track_f.columns

dataset = list()

for item,row in tracks_new.iterrows():
         
    dataset.append ({
                        
                            'artists': row['artists'],
                            'artists_ids': row['artist_ids'],
                            'country_mb': row['country_mb'],
                            'tags_lastfm': row['tags_lastfm'],
                            'album': row['album'],
                            'album_id': row['album_id'],
		            'disc_number': row['disc_number'],                       
                            'id': row['id'],
                            'name': row['name'],
                            'track_number': row['track_number'],
                            'year': row['year'],
                            'release_date': row['release_date'],
                            'explicit': row['explicit'],
                            'danceability': row['danceability'],
                            'energy': row['energy'],
                            'valence':row['valence'],
                            'liveness': row['liveness'],
                            'speechiness': row['speechiness'],
                            'listeners_lastfm':row['listeners_lastfm'],             
                            'music_atributes': {       
                                'duration_ms' : row['duration_ms'],
                                'tempo' : row['tempo'],
                                'acousticness' : row['acousticness'],
                                'loudness' : row['loudness'],
                                'time_signature' : row['time_signature'],
                                'key' : row['key'],
                                'instrumentalness' : row['instrumentalness'],
                                'mode' : row['mode']
                            }   
                        
                    })
        
spotify_musicdata.insert_many(dataset)