import os
import sys

import pafy

print("Хотите скачать видео или аудио с YouTube? Просто введите URL ниже...")
url = input("Введите URL: ")

print("Что-бы скачать видео введите: 1 | Что-бы скачать аудио введите: 2 ")
choice = input("Введите цифру: ")


def download(choice):
    try:
        v = pafy.new(url)

        if choice == "1":
            streams = v.streams
        elif choice == "2":
            streams = v.audiostreams
        else:
            sys.exit()

        print("Выберите желаемое качество видеоролика передав цифру. Пример: 1: ") if choice == "1" else print("Выберите желаемое качество аудио передав цифру. Пример: 2: ")

        available_streams = {}
        count = 1
        for stream in streams:
            available_streams[count] = stream
            print(f"{count}: {stream}")
            count += 1
        # print(available_streams)

        stream_count = int(input("Введите номер: "))
        d = streams[stream_count - 1].download()
        # print(d)
        if choice == "2":
            audio_extension = str(available_streams[stream_count])
            audio_extension = audio_extension.split("@")[0].split(":")[1]

            file_name = v.title
            music_file = f"{file_name}.{audio_extension}"
            base = os.path.splitext(music_file)[0]
            os.rename(music_file, base + ".mp3")
            print(music_file, base)
        print("Скачивание успешно завершено!")
    except:
        print("Упс...Проверьте данные")


download(choice)