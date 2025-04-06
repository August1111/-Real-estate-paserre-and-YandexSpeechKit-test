from speechkit import model_repository, configure_credentials, creds
from striprtf.striprtf import rtf_to_text

# Аутентификация через API-ключ.
configure_credentials(
   yandex_credentials=creds.YandexCredentials(
      api_key='AQVNw4jtPThxtQNjBeA067HSB6ww_P3_H-krVYiM'
   )
)

def speech(text,i) :
   model = model_repository.synthesis_model()

   model.voice = 'kirill'

   model.unsafe_mode = True

   model.speed = 1.2

   result = model.synthesize(text, raw_format=False)  # returns audio as pydub.AudioSegment
   result.export(f'G:/speech/output_{i}.wav', format='wav')


def split_text(text, length):
   return [text[i:i + length] for i in range(0, len(text), length)]


# Пример использования
with open('C:/Users/artem/YandexDisk/Literature/Сова/test.scriv/Files/Data/E9D8987C-243A-446E-B889-A8A4E3B0FEFC/content.rtf', 'r') as file:
   rtf_text = file.read()  # Замените это своим текстом
   text = rtf_to_text(rtf_text)

length = 4000
text_array = split_text(text, length)

for i in range(len(text_array)):
   speech(text_array[i],i)

from pydub import AudioSegment
import os

 #  Укажите путь к папке
directory_path = 'G:/speech'  # Пример: '/path/to/your/directory'

# Укажите расширение файла
file_extension = '.wav'  # Пример: '.jpg', '.pdf', и т.д.

# Подсчёт количества файлов с указанным расширением
file_count = sum(1 for file in os.listdir(directory_path) if file.endswith(file_extension))

combined_audio = AudioSegment.from_file(f"G:/speech/output_0.wav")

# Склеивание аудиозаписей
for i in range(1,file_count) :
    audio1 = AudioSegment.from_file(f"G:/speech/output_{i}.wav")
    combined_audio = combined_audio + audio1

# Экспорт результата
combined_audio.export("G:/speech/combined/combined_audio_16.wav", format="wav")

