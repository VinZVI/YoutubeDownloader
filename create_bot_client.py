import os

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from telethon import TelegramClient

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone = '+79151610210'
client = TelegramClient('testbot', api_id, api_hash)

# def main():
client.start()
# async def on_start_client():
print('Клиент вышел в онлаин')
# me = client.get_me()


# asyncio.run(main())
storage = MemoryStorage()  # запускаем место для хранени я ответов
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=storage)
