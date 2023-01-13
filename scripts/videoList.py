import creds as creds
import requests
import json
from pprint import pp 

channel_id = "UCESLZhusAkFfsNsApnjF_Cg"
url = f'https://www.googleapis.com/youtube/v3/search?key={creds.api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20'
response = requests.get(url)

#sub = int(response['items'][0]['statistics']['subscriberCount'])
data = response.json()

total_videos = int(data["pageInfo"]['totalResults'])


link = f'https://www.googleapis.com/youtube/v3/search?key={creds.api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults={total_videos}'
link_data = requests.get(link).json()


titles = (link_data["items"][0]["snippet"]["title"])

for titles in range(link_data):
    titles = (link_data["items"][0]["snippet"]["title"])
    print(titles)