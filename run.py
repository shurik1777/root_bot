import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv

from app.handlers import router

load_dotenv(find_dotenv())
bot = Bot(token=getenv('TOKEN'),
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
