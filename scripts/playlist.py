import scripts.creds as creds
from googleapiclient.discovery import build 
import json

from datetime import date

today = date.today()



#keys
api_key = creds.api_key

#youtube api service
youtube = build('youtube', 'v3', developerKey=api_key)

playlist_request = youtube.playlists().list(
    part='contentDetails, snippet',
    channelId='UCESLZhusAkFfsNsApnjF_Cg'
)

playlist_response = playlist_request.execute()



#print(playlist_response)

#loop over items
for item in playlist_response['items']:
     print(f"{item}\n")
print(f"Playlist Count: {len(item)}")
   
