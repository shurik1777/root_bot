from aiogram import Router, F
from aiogram.types import Message
from config_reader import bot

files_d = Router()


@files_d.message(F.photo)
async def download_photo(message: Message):
    await bot.download(
        message.photo[-1],
        destination=f"D:\\Ucheba\\TG_BOTS\\test_bot\\app\\{message.photo[-1].file_id}.jpg"
    )


@files_d.message(F.sticker)
async def download_sticker(message: Message):
    await bot.download(
        message.sticker,
        # для Windows пути надо подправить
        destination=f"D:\\Ucheba\\TG_BOTS\\test_bot\\app\\{message.sticker.file_id}.webp"
    )
