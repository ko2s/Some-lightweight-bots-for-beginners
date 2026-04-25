import os
from pytube import YouTube
import instaloader
import yt_dlp as youtube_dl
def download_youtube_video(url, download_path):
    yt = YouTube(url)
    # Filter for progressive streams (containing both video and audio) in MP4 format
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    # Download the video
    stream.download(download_path)
    print(f"Downloaded: {yt.title}")
def download_instagram_video(url, download_path):
    L = instaloader.Instaloader(download_videos=True)
    post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
    L.download_post(post, download_path)
    print(f"Downloaded: {post.title}")
def download_with_youtube_dl(url, download_path):
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
def main():
    url = input("Enter the URL of the video: ")
    download_path = input("Enter the download path: ")
    if 'youtube.com' in url or 'youtu.be' in url:
        download_youtube_video(url, download_path)
    elif 'instagram.com' in url:
        download_instagram_video(url, download_path)
    else:
        download_with_youtube_dl(url, download_path)
if __name__ == "__main__":
    main()