import asyncio
from aiogram import Dispatcher, Bot
from handlers import userhandler
from config.config import load_config


async def main():
    config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(userhandler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
