import os
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip, concatenate_videoclips

# قائمة الروابط
video_urls = [
    "https://youtu.be/jsHrrjlAVUA?si=gVL9YdRIq4Z1bUkw",
    "https://youtu.be/dzygU6zj9Dk?si=XC98z5LLm8_GZ44e",
    "https://youtu.be/nZQb5ugLNrk?si=Eeo65PEwaMDJwDZX",
    "https://youtu.be/_aZYeSAT3nY?si=QXzUR9DR5mYvXZOZ",
    "https://youtu.be/MEMcpPEXF4w?si=iEjqEOFjPwwFulmF",
    "https://youtu.be/8tRg0IzLedM?si=-QHRGztpCfexGIZB",
    "https://youtu.be/pha_qhpOYkY?si=hKzOhLuAuBuTg8sz"
]

# مجلد لحفظ الفيديوهات
download_folder = "downloaded_videos"
os.makedirs(download_folder, exist_ok=True)

# إعدادات yt-dlp
ydl_opts = {
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'format': 'bestvideo+bestaudio/best'
}

# تنزيل الفيديوهات
print("Downloading videos...")
downloaded_files = []
with YoutubeDL(ydl_opts) as ydl:
    for url in video_urls:
        info = ydl.extract_info(url, download=True)
        downloaded_files.append(ydl.prepare_filename(info))

print("All videos downloaded!")

# دمج الفيديوهات
print("Merging videos...")
clips = [VideoFileClip(file) for file in downloaded_files]
final_clip = concatenate_videoclips(clips, method="compose")

# حفظ الفيديو النهائي
output_file = "merged_video.mp4"
final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

# تنظيف الموارد
final_clip.close()
for clip in clips:
    clip.close()

print(f"Videos merged successfully into {output_file}!")