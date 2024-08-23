import pandas as pd
import ast

document_path = "/mnt/c/Users/leoni/Desktop/Project_translate_videos/subtitles.txt"
file = open(document_path, 'r')

# Read all lines in document
lines = file.readlines()

data = []
# Process everyline to create a lsit of dictionaries
for line in lines:
    # print(ast.literal_eval(line))
    data.append(ast.literal_eval(line))

print(data)
# print(data)

document_path = "/mnt/c/Users/leoni/Desktop/Project_translate_videos/subtitles.txt"
file = open(document_path, 'r')

# Read all lines in document
lines = file.readlines()

data = []
# Process everyline to create a lsit of dictionaries
for line in lines:
    # print(ast.literal_eval(line))
    data.append(ast.literal_eval(line))

print(data)
# print(data)

from translate import Translator
translator = Translator(to_lang="spanish")

def translate_text(text):
    try:
        translation = translator.translate(text)
        print(translation)
        return translation
    except Exception as e:
        print(f"Error translating text: {text}\n{e}")
        
# Aplica la traducción+
df['translated_text'] = df['text'].apply(translate_text)

# Imprime el DataFrame con las traducciones
print(df)