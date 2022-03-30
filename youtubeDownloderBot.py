from aiogram.utils import executor

from create_bot_client import dp
from handlersBot import register_handlers_bot

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="mylog.log",
#     format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
#     datefmt='%H:%M:%S',
# )


""" Запускаем хендлеры бота"""
register_handlers_bot(dp)


async def on_startup(_):
    print('Бот вышел в онлайн')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
