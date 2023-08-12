import googleapiclient.discovery

KEY = 'AIzaSyAgkB_zpAQg_ayoT0qVZVtyD7NNOodWPZA'
CHANNEL_NAME = 'myrusakov'#'LojazDmitry'

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=KEY)


def get_video_ids_from_channel(channel_name):
    playlist_id = get_playlist_id(channel_name)
    response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=10
    ).execute()
    print(response)

def get_playlist_id(channel_name):
    # получаем информацию о канале
    response = youtube.channels().list(
        part="contentDetails",  # получаем только информацию о контенте
        forUsername=channel_name
    ).execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    videos = get_video_ids_from_channel(CHANNEL_NAME)
    # print_videos_info(videos)
