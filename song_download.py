import yt_dlp
import os

def download_from_urls(urls, download_type="audio"):
    # Ensure output folder exists
    if download_type == "audio":
        output_dir = "songs"
        os.makedirs(output_dir, exist_ok=True)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        }
    elif download_type == "video":
        output_dir = "videos"
        os.makedirs(output_dir, exist_ok=True)
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # best quality
            'merge_output_format': 'mp4',          # ensure mp4 output
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        }
    else:
        raise ValueError("download_type must be 'audio' or 'video'")

    for url in urls:
        print(f"Downloading {download_type} from: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # needs list, not string

# Example usage:
# download_from_urls(["https://www.youtube.com/watch?v=abcd1234"], "audio")
# download_from_urls(["https://www.youtube.com/watch?v=abcd1234"], "video")
