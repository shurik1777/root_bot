"""Точка входа и запуска, так же подключения обработчика событий и пр."""
import asyncio
import logging
from datetime import datetime

from aiogram import Dispatcher

from app.d_files import files_d
from app.h_files import files
from app.handlers import router
from app.handlers_kb_start import kbd
from app.keybords_url import kbd_two
from app.keybords_callback import kbd_three
from config_reader import bot


async def main():
    """
    Функция подключения через Диспетчер обработчиков событий и пр.
    """
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(files)
    dp.include_router(files_d)
    dp.include_router(kbd)
    dp.include_router(kbd_two)
    dp.include_router(kbd_three)
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
