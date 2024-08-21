from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=QvSgUdx0ncY"
save_path = "/mnt/c/Users/leoni/Desktop/Projecto_translate_videos/Downloads"
audio_path = "/mnt/c/Users/leoni/Desktop/Projecto_translate_videos/Audios"
video_path = "/mnt/c/Users/leoni/Desktop/Projecto_translate_videos/Videos"
 
yt = YouTube(url, on_progress_callback = on_progress)
# Convertir el título a minúsculas
yt_title_lower = yt.title.lower()

# Dividir el título en palabras y seleccionar las tres primeras
first_three_words = yt_title_lower.split()[:3]

# Unir las tres primeras palabras con guiones bajos
yt.title = "_".join(first_three_words)

print(yt.title)


# Video
video = yt.streams.get_highest_resolution()
video.download(output_path = video_path)

audio = yt.streams.get_audio_only()
# ys.download(output_path = save_path)
audio.download(output_path = audio_path, mp3=True)