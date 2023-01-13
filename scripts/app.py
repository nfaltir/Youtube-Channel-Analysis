import scripts.creds as creds
from googleapiclient.discovery import build 
import json
import streamlit as st
from datetime import date

today = date.today()



#keys
api_key = creds.api_key

#youtube api service
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(
    part='statistics, contentDetails',
    id='UCESLZhusAkFfsNsApnjF_Cg'
)


playlist_request = youtube.playlists().list(
    part='statistics, contentDetails',
    channelId='UCESLZhusAkFfsNsApnjF_Cg'
)

response = request.execute()
for i in response["items"]:
    channel_id = i['id']
    etag = i['etag']

playlist_response = playlist_request.execute()


sub = int(response['items'][0]['statistics']['subscriberCount'])
vid = int(response['items'][0]['statistics']['videoCount'])
views = int(response['items'][0]['statistics']['viewCount'])
  
avg_view = round(views/vid,2)


st.header("Allin You Statistics")

st.write(f"\nChannel Id: {channel_id}")
st.write(f"etag: {etag}\n")

st.write(f"\nTotal Subscribers: {sub:,}")
st.write(f"\nTotal Videos: {vid}")
st.write(f"\nTotal Views: {views:,}")
st.write(f"\nAverage view per video: {avg_view:,}")
st.write(f"Report Generated on: {today}")

#print("\n")
     
#print(f"\nChannel Id: {channel_id}")
#print(f"etag: {etag}\n")

#print(f"\nTotal Subscribers: {sub:,}")
#print(f"\nTotal Videos: {vid}")
#print(f"\nTotal Views: {views:,}")
#print(f"\nAverage view per video: {avg_view:,}")

print("\n")

