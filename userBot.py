import os

from telethon import TelegramClient

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone = '+79151610210'
client = TelegramClient('testbot', api_id, api_hash)

# def main():
client.start()

# me = client.get_me()
print('Клиент вышел в онлаин')

# asyncio.run(main())
