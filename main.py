import googleapiclient.discovery

KEY = ''
CHANNEL_NAME = 'myrusakov' #'LojazDmitry'

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=KEY)


def get_video_ids_from_channel(channel_name):
    playlist_id = get_playlist_id(channel_name)
    response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=10
    ).execute()
    ids = []
    for video in response['items']:
        ids.append(video['snippet']['resourceId']['videoId'])
    return ids

def get_playlist_id(channel_name):
    # получаем информацию о канале
    response = youtube.channels().list(
        part="contentDetails",  # получаем только информацию о контенте
        forUsername=channel_name
    ).execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def print_videos_info(videos_ids):
    response = youtube.videos().list(
        part="statistics, snippet",
        id=','.join(videos_ids)
    ).execute()
    for video in response['items']:
        print('Название:', video['snippet']['title'])
        print('Просмотры:', video['statistics']['viewCount'])
        print('Лайков:', video['statistics']['likeCount'])
        #print('Дизлайков:', video['statistics']['dislikeCount'])
        print('-------------------------------------')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    videos = get_video_ids_from_channel(CHANNEL_NAME)
    print_videos_info(videos)
