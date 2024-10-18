"""То, что я называю переработанным кодом с самого начала"""
from aiogram import Router  # Импорт роутера для начала работы с файлом обработчиком событий
from aiogram.filters import CommandStart, Command  # Фильтры
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update, \
    CallbackQuery  # Типы

from utils.kb import create_keyboard, \
    create_keyboard_in  # Импорт отдельно взятой функции для подключения одинаковых логик

kbd = Router()


@kbd.message(CommandStart())
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


@kbd.message(Command("go"))
async def push_me(message: Message):
    """ Функция для начала взаимодействия """
    buttons = [
        InlineKeyboardButton(text="Нажми меня!",
                             callback_data="button_pressed")
    ]
    keyboard = create_keyboard_in(buttons)
    await message.answer('Привет! Нажми на кнопку ниже:',
                         reply_markup=keyboard)


@kbd.callback_query(lambda c: c.data == 'button_pressed')
async def button_push(callback: CallbackQuery):
    """ Отвечаем на нажатие кнопки """
    await callback.message.edit_text(
        text="Ты нажал кнопку!")
    await callback.answer()
