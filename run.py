import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher
from app.handlers import user, admin
import os

async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(admin.router, user.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")