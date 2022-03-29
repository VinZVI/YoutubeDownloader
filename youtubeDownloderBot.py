from aiogram.utils import executor

from handlersClent import register_handlers_client, dp


# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="mylog.log",
#     format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
#     datefmt='%H:%M:%S',
# )





async def on_startup(_):
    print('Бот вышел в онлайн')


register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
