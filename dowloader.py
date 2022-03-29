import os

from userBot import client


async def download(get_url_download, urlPafy):
    # try:

    get_url_download.download()
    file_name = urlPafy.title
    if "audio" == str(get_url_download).split(":")[0]:
        audio_extension = str(get_url_download).split("@")[0].split(":")[1]

        music_file = f"{file_name}.{audio_extension}"
        base = os.path.splitext(music_file)[0]
        os.rename(music_file, base + ".mp3")
        await client.send_file('@Date_countBot', f'{file_name}.mp3')
        print("Скачивание успешно завершено!")
    else:
        await client.send_file('@Date_countBot', f'{file_name}.mp4')
        print("Скачивание успешно завершено!")
    # except:
    # print("Упс...Проверьте данные")
