from re import fullmatch

import pafy
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from youtubeDownloderBot import bot

""" Машина состояний диалога """


class FSMclient(StatesGroup):
    urlState = State()  # сотояние выбора URL
    choiceState = State()  # выбор видео или аудио
    qualityState = State()  # выбор качества видео или аудио


# from aiogram.types import ReplyKeyboardRemove # класс удаляет клавиатуру

""" Команда /Start - начало диалога"""


# @dp.message_handler(commands='start', state=None)
async def commands_start(message: types.Message):
    # начало для приватного чата
    if message.chat.type == types.ChatType.PRIVATE:
        await FSMclient.urlState.set()  # устанавливаем состояние бота urlState
        await message.reply('Хотите скачать видео или аудио с YouTube? Просто введите URL:')
    # если бот добавлен в группу
    else:
        bot_info = await bot.get_me()  # Получаем информацию о нашем боте
        keyboard = types.InlineKeyboardMarkup()  # Создаём клавиатуру с URL-кнопкой для перехода в ЛС
        move_to_dm_button = types.InlineKeyboardButton(text="Перейти в ЛС",
                                                       url=f"t.me/{bot_info.username}?start=anything")
        keyboard.add(move_to_dm_button)
        await message.reply("Общение с ботом через ЛС, напишите ему:", reply_markup=keyboard)


""" Ловим Url и записываем его в память"""


# @dp.message_handler(state=FSMclient.urlState)
async def get_url(message: types.Message):
    if not fullmatch(r"(https?:\/\/)?(\www\.youtube)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?.*", message.text):
        await message.reply('Пожалуйста. Введие данные в формате Url - https://www.youtube.com/...')
        return
    global urlPafy
    urlPafy = pafy.new(message.text)
    await FSMclient.next()
    buttons = [
        types.InlineKeyboardButton(text="Видео", callback_data="choice_video"),
        types.InlineKeyboardButton(text="Аудио", callback_data="choice_audio"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.reply('В каком формате выхотите скачать?\n', reply_markup=keyboard)


""" Ловим выбор формата video или audio
    Получаем качество видео или аудио для выбора"""


# @dp.callback_query_handler(Text(startswith="choice_"), state=FSMclient.choiceState)
async def callbacks_choice(call: types.CallbackQuery):
    try:
        # Парсим строку и извлекаем действие, например `choice_video` -> `video`
        action = call.data.split("_")[1]
        if action == "video":
            streams = urlPafy.streams
            text = "Выберите желаемое качество видеоролика:\n"
        elif action == "audio":
            streams = urlPafy.audiostreams
            text = "Выберите желаемое качество аудио:\n"

        available_streams = {}
        count = 1
        keyboard = types.InlineKeyboardMarkup()
        for stream in streams:
            available_streams[count] = stream
            # print(f"{count}: {stream}")
            buttons = types.InlineKeyboardButton(text=f"{count}: {stream}", callback_data=f"{count}")
            keyboard.add(buttons)
            count += 1

        await call.message.answer(text, reply_markup=keyboard)
        # Не забываем отчитаться о получении колбэка
        await call.answer()
        # Если бы мы не меняли сообщение, то можно было бы просто удалить клавиатуру
        # вызовом await call.message.delete_reply_markup().
    except:
        await call.message.answer("Упс...Проверьте данные")
        await call.answer()


""" Ловим выбор качества видео или аудио
    Скачиваем видео или аудио и отправляем пользователю """


# @dp.callback_query_handler(Text(startswith="choice_"), state=FSMclient.qualityState)
# async def callbacks_quality(call: types.CallbackQuery):


# Хэндлер на текстовое сообщение с текстом “Отмена”
# @dp.message_handler(lambda message: message.text == "Отмена")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Действие отменено. Введите /start, чтобы начать заново.", \
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True). \
                         add(KeyboardButton('/start')))
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands='start')
    dp.register_message_handler(get_url, commands='start')
    dp.register_callback_query_handler(callbacks_choice, Text(startswith="choice_"), state=FSMclient.choiceState)
    dp.register_message_handler(action_cancel, commands='отмена')
    dp.register_message_handler(action_cancel, Text(equals='отмена', ignore_case=True))
