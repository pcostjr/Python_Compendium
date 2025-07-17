#api_search.py
# description: A simple API tool to test and ensure Spotify API keys are working as expected.
# author: pcostjr
# created: 7.17.2025
# last update: 7.17.2025

# import package from pip package repository
import spotipy
from spotipy.oauth2 import SpotifyOAuth as Auth

# identification for auth
cid = ""
secret = ""
redirect = ""

# authenticate to Spotify
sp_oauth = Auth(client_id=cid,
                client_secret=secret,
                redirect_uri=redirect,
                scope='user-library-read')
sp = spotipy.Spotify(auth_manager=sp_oauth)

print("Connected to Spotify API, Searching for \"Jungle Drum & Bass Mix\"\n")
# get the cached token

# Post a GET request using the keyword, specifically on playlists
# parse the results into a list called items
result = sp.search(q='playlist= Jungle Drum & Bass Mix', type='playlist')
items = result['playlists']['items']
for item in items:
    # spotify likes to auto-generate some playlists so this will avoid them and only print out our target ones
    if item is not None:
        # format the data in the item so its readable
        print(f"Playlist Name: {item['name']}\n"
              f"Created By: {item['owner']['display_name']}\n"
              f"URL: {item['owner']['external_urls']['spotify']}\n"
              f"Number of tracks: {item['tracks']['total']}")
        print()
