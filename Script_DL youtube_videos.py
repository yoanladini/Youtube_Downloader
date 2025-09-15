import yt_dlp
def download_video(url, output_path='.'):
    """
    Downloads a video from the given URL using yt-dlp.

    Args:
        url (str): The URL of the video to download.
        output_path (str): The directory where the video will be saved.
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,  # Prevent downloading entire playlists if a playlist URL is given
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    save_directory = input("Enter the save directory (press Enter for current directory): ") or '.'
    
    download_video(video_url, save_directory)
    print(f"Video download initiated for {video_url} to {save_directory}")