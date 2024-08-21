from youtube_transcript_api import YouTubeTranscriptApi as yta
from urllib.parse import urlparse
from urllib.parse import parse_qs

url = "https://www.youtube.com/watch?v=PY_N1XdFp4w"
# Paso 1: Configuración del video de YouTube
parsed = urlparse(url)
video_id = parse_qs(parsed.query)["v"][0]
# video_id = "UTgnOwpafpw"


# Paso 2: Extraer la transcripción
data = yta.get_transcript(video_id, languages=['es', 'en'])

# Paso 3: Concatenar las líneas de la transcripción en un solo string
transcript = ''
for value in data:
    transcript += value.get('text', '') + ' '

# Paso 4: Guardar la transcripción en un archivo .txt
ruta_transcript = "Desktop/Projecto_translate_videos/transcript/laos.txt"
with open(ruta_transcript, "w", encoding='utf-8') as file:
    file.write(transcript)

# # Paso 5: Leer el contenido del archivo .txt
# with open(ruta_transcript, 'r', encoding='utf-8') as file:
#     texto = file.read()

# # Paso 6: Inicializar el corrector gramatical
# parser = GingerIt()

# # Paso 7: Corregir el texto
# resultado = parser.parse(texto)
# texto_corregido = resultado['result']

# # Paso 8: Guardar el texto corregido en un nuevo archivo .txt
# ruta_corregida = "Desktop/Projecto_translate_videos/transcript/laos_corregido.txt"
# with open(ruta_corregida, 'w', encoding='utf-8') as file:
#     file.write(texto_corregido)

# print(f"El documento ha sido corregido y guardado como '{ruta_corregida}'.")
