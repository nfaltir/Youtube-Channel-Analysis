import scripts.creds as creds
import requests
import json

video_id = input("Enter video id: ")

url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={creds.api_key}"
response = requests.get(url)

#sub = int(response['items'][0]['statistics']['subscriberCount'])
data = response.json()

#Report
try:
    view_count = int(data["items"][0]["statistics"]["viewCount"])
    like_count = int(data["items"][0]["statistics"]["likeCount"])
    comment_count = int(data["items"][0]["statistics"]["commentCount"])
    favorite_count = int(data["items"][0]["statistics"]["favoriteCount"])

    likeRatio = round((like_count/view_count)*100,2)
    commentRatio = round((comment_count/view_count)*100,2)    
except:
    print(f"Error: {KeyError}")


print(f"\nVideo ID: {video_id}")
print(f"View Count: {view_count:,} ")
print(f"Like Count: {like_count:,} ") 
print(f"Comment Count: {comment_count:,} ")
print(f"Favorite Count: {favorite_count:,} \n")

print(f"\nLikes & Views Ratio: {likeRatio}% ")
print(f"Comments & Views Ratio: {commentRatio}% \n")


#print(data)