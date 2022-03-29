# from userBot import client
import os


def download(get_url_download, urlPafy):
    # try:

    d = get_url_download.download()

    if "audio" == str(get_url_download).split(":")[0]:
        audio_extension = str(get_url_download).split("@")[0].split(":")[1]
        file_name = urlPafy.title
        music_file = f"{file_name}.{audio_extension}"
        base = os.path.splitext(music_file)[0]
        os.rename(music_file, base + ".mp3")
        # client.send_file('@Date_countBot', f'/YoutubeDownloader/{file_name}.mp3')
        print("Скачивание успешно завершено!")
    else:
        # client.send_file('@Date_countBot', f'/YoutubeDownloader/{file_name}.mp4')
        print("Скачивание успешно завершено!")
    # except:
    # print("Упс...Проверьте данные")
