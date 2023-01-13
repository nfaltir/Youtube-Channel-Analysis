from worker import youtubedata
import creds


API_KEY = creds.api_key
channel_id = "UCESLZhusAkFfsNsApnjF_Cg"
yt = youtubedata(API_KEY, channel_id)
yt.extract_all()
yt.dump()  # dumps to .json