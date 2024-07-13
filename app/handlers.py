from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from datetime import datetime


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
