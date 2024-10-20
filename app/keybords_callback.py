"""Working with keyboard callback"""
from random import randint

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, KeyboardButton
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

kbd_three = Router()


@kbd_three.message(Command("random"))
async def cmd_random(message: Message):
    """Random keyboard"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    """Использование suppress для игнорирования TelegramBadRequest: Внутри блока with suppress(TelegramBadRequest)
    мы пытаемся отправить сообщение. Если возникает исключение TelegramBadRequest,
    оно будет проигнорировано, и выполнение программы продолжится.
    Это значит, что если команда не удалась, бот не будет прерывать свою работу,
    а просто продолжит выполнение следующего кода.
    """
    with suppress(TelegramBadRequest):
        await message.answer(
            "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
            reply_markup=builder.as_markup()
        )


@kbd_three.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery):
    """Sends random value"""
    """Обработка нажатия на Callback-кнопку выполняется с помощью handler на callback_query.
    Важно определить правильное значение data для кнопки."""
    await callback.message.answer(str(randint(1, 10)))
    """при использовании Callback-кнопок, важно подтвердить доставку callback,
    чтобы избежать появления значка ожидания на экране пользователя.
    Это можно сделать с помощью метода answer() у callback."""
    await callback.answer()


"""
### Когда использовать suppress:

- Используйте suppress, когда вы хотите игнорировать временные ошибки
или когда ошибка не критична для дальнейшего выполнения кода.
- Будьте осторожны с использованием suppress, чтобы не скрыть ошибки,
которые стоят внимания; это может затруднить отладку кода.
"""


@kbd_three.message(Command("core"))
async def reply_builder(message: Message):
    """Работа с RKB создает клавиатуру, на которой числа от 1 до 16 располагаются в виде таблицы 4×4,
    что обеспечивает более удобный выбор пользователю."""
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer(
        "Выберите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
