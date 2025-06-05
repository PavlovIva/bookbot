from aiogram import Bot
from aiogram.types import Message
from config.config import load_config

config = load_config()
bot = Bot(token=config.tg_bot.token)


async def download_book(msg: Message):
    file = await bot.get_file(msg.document.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, 'books/' + msg.document.file_name)



def read_the_book(file_name):
    try:
        with open('books/' + file_name, encoding='windows-1251') as f:
            return f.read(1000)
    except UnicodeDecodeError:
            with (open('books/' + file_name, encoding='UTF-8')) as f:
                return f.read(1000)



