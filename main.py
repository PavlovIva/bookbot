from aiogram import Dispatcher, Bot
import asyncio
from config.config import Config, load_config
import handlers.user_handlers

async def main() -> None:

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(handlers.user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())


