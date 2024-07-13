import asyncio
import logging
from datetime import datetime

from aiogram import Dispatcher


from app.handlers import router
from config_reader import bot


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
