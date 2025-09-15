import yt_dlp

urls = ["https://www.youtube.com/watch?v=GYtBoxGB6Wo"]
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'songs/%(title)s.%(ext)s',  # Output file name
}
for url in urls:
    print (f"Downloading audio from: {url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio...")
        ydl.download(url)
