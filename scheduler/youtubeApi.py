# Main file for everything

from api.models import Youtube_videos
from datetime import datetime, timedelta
# Google API
from apiclient.discovery import build
import apiclient

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def fetch():
    search_response = {}
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    # Get Current Time and previous time
    current_time = datetime.now()
    previous_time = current_time - timedelta(minutes=5)

    # Add Your input over here

    # Max Result will be directly proptional to options
    options = 'official'
    s_part = 'snippet'
    max_Results = 10
    order = 'date'
    latest_published = previous_time.replace(microsecond=0).isoformat() + 'Z'
    isValid = 0

    # Add your own key here
    # It also support multiple keys
    DEVELOPER_KEY = [
        'sss',
        'AIzaSyA6KBXLgsP4--wr5mXtzPhWOJAQCsuJncWrE',
        'AIzaSyA6KBXLgsP4wr5mXtzPhWOJAQCsuJncWrE',
    ]
    for key in DEVELOPER_KEY:
        # Error handling
        try:
            youtube = build(YOUTUBE_API_SERVICE_NAME,
                            YOUTUBE_API_VERSION,
                            developerKey=key)
            search_response = youtube.search().list(
                q=options,
                part=s_part,
                maxResults=max_Results,
                order='date',
                publishedAfter=latest_published).execute()
            isValid = 1
        except apiclient.errors.HttpError as err:
            code = err.resp.status

            if not (code == 400 or code == 403):
                break
        if isValid:
            break
    if isValid:
        for item in search_response['items']:
            video_id = item['id']["videoId"]
            video_publishedDateTime = item['snippet']['publishedAt']
            video_title = item['snippet']['title']
            video_description = item['snippet']['description']
            video_thumb_urls = item['snippet']['thumbnails']['default']['url']
            channel_id = item['snippet']['channelId']
            channel_title = item['snippet']['channelTitle']
            Youtube_videos.objects.create(
                video_id=video_id,
                video_title=video_title,
                video_description=video_description,
                channel_id=channel_id,
                channel_title=channel_title,
                video_publishedDateTime=video_publishedDateTime,
                video_thumb_urls=video_thumb_urls,
            )
