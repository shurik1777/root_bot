from aiogram import Router, F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command
files = Router()


@files.message(F.animation)
async def echo_gif(message: Message):
    """Echo gif message"""
    await message.reply_animation(message.animation.file_id)


@files.message(Command('images'))
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []
    """В photo_id у нас присваивается массив идентификаторов, но нам не нужно маленькое изображение,
    лучше же в отличном качестве, поэтому чтобы получить идентификатор высокого качества,
    мы ставим там "[3]" чтобы взять его из этого массива,
    точно не помню, но значит он находится на 4 позиции,
    Т. к. Массивы с 0. Если короче, то у Аргумента photo мы берём только 4-ый file_id
    или как тут у груши result.photo[-1] - срезом"""

    # Чтобы продемонстрировать BufferedInputFile, воспользуемся "классическим"
    # открытием файла через `open()`. Но, вообще говоря, этот способ
    # лучше всего подходит для отправки байтов из оперативной памяти
    # после проведения каких-либо манипуляций, например, редактированием через Pillow
    # with open("/app/my_foto.jpg", "rb") as image_from_buffer:
    #     result = await message.answer_photo(
    #         BufferedInputFile(
    #             image_from_buffer.read(),
    #             filename="image from buffer.jpg"
    #         ),
    #         caption="Изображение из буфера"
    #     )
    #     file_ids.append(result.photo[-1].file_id)

    # Отправка файла из файловой системы
    image_from_pc = FSInputFile(r"D:\Ucheba\TG_BOTS\test_bot\app\my_foto.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла по ссылке, но только с https сайтов
    image_from_url_https = URLInputFile("https://static.tildacdn.com/tild3836-6462-4533-a164-653964646233/DSC06622.jpg")
    result = await message.answer_photo(
        image_from_url_https,
        caption="Изображение по HTTPS ссылке"
    )
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла по ссылке, но только с http сайтов
    image_from_url = URLInputFile("http://lamcdn.net/lookatme.ru/post-cover/zW9lKFdbXYkHuKkbGegvow-default.jpg")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    file_ids.append(result.photo[-1].file_id)
    await message.answer("Отправленные файлы:\n" + "\n".join(file_ids))


@files.message(Command("gif"))
async def send_gif(message: Message):
    await message.answer_animation(
        animation="AgACAgIAAxkDAAM6ZpN1XHLKzir-cAEeITwkl-XyI8UAAl3gMRu69ZhIdOF8ah3R23sBAAMCAANtAAM1BA",
        caption="Я сегодня:",
        show_caption_above_media=True
    )
