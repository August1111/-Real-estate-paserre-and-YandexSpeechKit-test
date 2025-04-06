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