#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install spotipy


# In[6]:


import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
cid = '7d120b7f7300426a8c0ae14857db1627'
secret = '2f2306eaacdc4698bc577fa4fd79c6a1'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)


# In[3]:


def call_playlist(creator, playlist_id):
    
    #step1

    playlist_features_list = ["artist","album","track_name",  "track_id","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]
    
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
    #step2
    
    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)

    #Step 3
        
    return playlist_df


# In[7]:


call_playlist("spotify","2RV47uPPe7cREVOrCCcjLf")


# In[8]:


call_playlist("spotify","2RV47uPPe7cREVOrCCcjLf").to_csv(r'G:\My Drive\Cours\M2\S2\Machine Learning and Artificial Intelligence for Business\spotreco.csv')


# In[ ]:




