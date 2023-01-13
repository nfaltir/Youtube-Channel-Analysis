import creds as creds
from googleapiclient.discovery import build 
import json

from datetime import date

today = date.today()



#keys
api_key = creds.api_key

#youtube api service
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(
    part='statistics',
    id='UCESLZhusAkFfsNsApnjF_Cg'
)

response = request.execute()
for i in response["items"]:
    channel_id = i['id']
    etag = i['etag']





sub = int(response['items'][0]['statistics']['subscriberCount'])
vid = int(response['items'][0]['statistics']['videoCount'])
views = int(response['items'][0]['statistics']['viewCount'])
  
avg_view = round(views/vid,2)




print("\n")
     
print(f"\nChannel Id: {channel_id}")
print(f"etag: {etag}\n")

print(f"\nTotal Subscribers: {sub:,}")
print(f"Total Videos: {vid}")
print(f"Total Views: {views:,}")
print(f"Average view per video: {avg_view:,} \n")

print("\n")

