"""То, что я называю переработанным кодом с самого начала"""
from aiogram import Router  # Импорт роутера для начала работы с файлом обработчиком событий
from aiogram.filters import Command  # Фильтры
from aiogram.types import Message, KeyboardButton  # Типы

from utils.kb import create_keyboard  # Импорт отдельно взятой функции для подключения одинаковых логик

kbd = Router()


@kbd.message(Command("start"))
async def cmd_start_too(message: Message):
    """
    3 Кнопки при отлове события /start
    :param message: /start
    :return: Привет, ты кто?
    """
    """Третий способ, два других ниже они больше и не такие гибкие, но в чужом коде они будут"""
    keyboard = create_keyboard([
        [KeyboardButton(text="Робот")],
        [KeyboardButton(text="Не робот")],
        [KeyboardButton(text="Робот, но мне сказали я не робот")]
    ])
    await message.answer("Привет, ты кто?", reply_markup=keyboard)
    '''
async def cmd_start(message: Message):
    ## с переменной kb:
    kb = [
        [KeyboardButton(text="Робот")],
        [KeyboardButton(text="Не робот")],
        [KeyboardButton(text="Робот, но мне сказали я не робот")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    ## без переменной kb:
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Робот")],
        [KeyboardButton(text="Не робот")],
        [KeyboardButton(text="Робот, но мне сказали я не робот")]
    ])
    await message.answer("Привет, ты кто?", reply_markup=keyboard)
    '''
"""
- Создание функции для создания клавиатуры: Если вам понадобится создать подобные клавиатуры в разных местах кода,
 можно создать вспомогательную функцию, чтобы избежать дублирования.

Пример создания функции в Utils:

def create_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=buttons)
    
Пример использования функции в app: 
async def cmd_start(message: Message):
    keyboard = create_keyboard([
        [KeyboardButton(text="Робот")],
        [KeyboardButton(text="Не робот")],
        [KeyboardButton(text="Робот, но мне сказали я не робот")]
    ])
    await message.answer("Привет, ты кто?", reply_markup=keyboard)
"""

