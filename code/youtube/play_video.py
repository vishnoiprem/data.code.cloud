import vlc
import time
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import os


def get_video_url(youtube, video_id):
    request = youtube.videos().list(
        part="contentDetails",
        id=video_id
    )
    response = request.execute()
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url


def play_video(url, play_time_sec):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    media.get_mrl()
    player.set_media(media)
    player.play()
    time.sleep(1)  # Give time for the video to start

    start_time = time.time()
    while time.time() - start_time < play_time_sec:
        if player.get_state() == vlc.State.Ended:
            player.stop()
            player.play()
            time.sleep(1)  # Give time for the video to restart
        time.sleep(1)

    player.stop()


def schedule_videos(youtube, video_id, daily_play_hours, total_days):
    daily_play_time_sec = daily_play_hours * 3600  # Convert hours to seconds
    total_play_time_sec = daily_play_time_sec * total_days

    end_time = datetime.datetime.now() + datetime.timedelta(days=total_days)
    video_url = get_video_url(youtube, video_id)
    while datetime.datetime.now() < end_time:
        print(f"Starting video playback for {daily_play_hours} hours.")
        play_video(video_url, daily_play_time_sec)
        print("Playback finished for today. Waiting until tomorrow.")
        time.sleep(24 * 3600 - daily_play_time_sec)  # Wait until the next day


def main():
    # Set up YouTube API credentials and build the service
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    if not os.path.exists(client_secrets_file):
        print(f"Error: {client_secrets_file} not found.")
        return

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)

    try:
        # Use run_local_server instead of run_console
        credentials = flow.run_local_server(port=0)
    except Exception as e:
        print(f"An error occurred
