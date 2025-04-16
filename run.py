from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
import asyncio
from app.user import user
from app.admin import admin
from app.database.models import async_main


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(user, admin)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)
    

async def on_startup(dispatcher):
    await async_main()


if __name__ == "__main__":
    try:
        print('Bot is running')
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
