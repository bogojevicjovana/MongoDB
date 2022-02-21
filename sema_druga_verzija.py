# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:50:14 2021

@author: PC
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymongo


client = pymongo.MongoClient()
db = client.data_spotify_
data_spotify_ = db.artists_data_set

track_f = pd.read_csv("tracks_features.csv", low_memory = False)
artists_f = pd.read_csv("artists.csv",low_memory = False )

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
                    'artist_info': {
                            'artists': row['artists'],
                            'artists_ids': row['artist_ids'],
                            'country_mb': row['country_mb'],
                            'tags_lastfm': row['tags_lastfm'],
                            
                            'album_info': {
                            'album': row['album'],
                            'album_id': row['album_id'],
		                    'disc_number': row['disc_number'],
                            
                            'track_info': {
                                    'id': row['id'],
                                    'name': row['name'],
                                    'track_number': row['track_number'],
                                    'year': row['year'],
                                    'release_date': row['release_date'],
                                    'track_feautures': {
    
                                            'explicit': row['explicit'],
                                            'danceability': row['danceability'],
                                            'energy': row['energy'],
                                            'valence':row['valence'],
                                            'liveness': row['liveness'],
                                            'speechiness': row['speechiness'],
                                            'listeners_lastfm':row['listeners_lastfm'],
                                            'duration_ms' : row['duration_ms'],
                                            'tempo' : row['tempo'],
                                            'acousticness' : row['acousticness'],
                                            'loudness' : row['loudness'],
                                            'time_signature' : row['time_signature'],
                                            'key' : row['key'],
                                            'instrumentalness' : row['instrumentalness'],
                                            'mode' : row['mode']
                                            
                                }
                            }
                        }
                    }
                })
        
data_spotify_.insert_many(dataset)