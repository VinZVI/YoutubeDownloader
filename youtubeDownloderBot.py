import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import handlersClent

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="mylog.log",
#     format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
#     datefmt='%H:%M:%S',
# )


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


handlersClent.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
