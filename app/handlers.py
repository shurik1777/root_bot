from datetime import datetime

from aiogram import Router, F, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag, Text
)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hello {message.from_user.first_name}')


# Хэндлер на команду /test1 подключаем через декоратор
@router.message(Command("test1"))
async def cmd_test1(message: Message):
    await message.reply("Test 1")


# Хэндлер на команду /test2 подключаем через точечную аннатацию
async def cmd_test2(message: Message):
    await message.reply("Test 2")


router.message.register(cmd_test2, Command("test2"))


@router.message(Command("answer"))
async def cmd_answer(message: Message):
    await message.answer("Это простой ответ")


@router.message(Command("reply"))
async def cmd_reply(message: Message):
    await message.reply('Это ответ с "ответом"')


@router.message(Command("dice"))
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command("add_to_list"))
async def cmd_add_to_list(message: Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@router.message(Command("show_list"))
async def cmd_show_list(message: Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


@router.message(Command("info"))
async def cmd_info(message: Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")


# Если не указать фильтр F.text,
# то хэндлер сработает даже на картинку с подписью /test
@router.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, <b>world</b>!",
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!",
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await message.answer("Сообщение с <u>HTML-разметкой</u>")
    # чтобы явно отключить форматирование в конкретном запросе,
    # передайте parse_mode=None
    await message.answer(
        "Сообщение без <s>какой-либо разметки</s>",
        parse_mode=None
    )


@router.message(Command("hello"))
async def cmd_hello(message: Message):
    """Не будет работать с ников м тегах"""
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML
    )


@router.message(Command("hello2"))
async def cmd_hello(message: Message):
    """Второе чуть сложнее, но более продвинутое:
    воспользоваться специальным инструментом,
    который будет собирать отдельно текст и отдельно
    информацию о том, какие его куски должны быть
    отформатированы."""
    content = Text(
        "Hello, ",
        Bold(message.from_user.full_name)
    )
    await message.answer(
        **content.as_kwargs()
    )


@router.message(Command("advanced_example"))
async def cmd_advanced_example(message: Message):
    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#test"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())


@router.message(F.text)
async def echo_with_time(message: Message):
    # Получаем текущее время в часовом поясе ПК
    time_now = datetime.now().strftime('%H:%M')
    # Создаём подчёркнутый текст
    added_text = html.underline(f"Создано в {time_now}")
    # Отправляем новое сообщение с добавленным текстом
    await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML")
