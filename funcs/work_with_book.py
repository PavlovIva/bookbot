from aiogram import Bot
from aiogram.types import Message
from config.config import load_config

config = load_config()
bot: Bot = Bot(token=config.tg_bot.token)


async def download_book(msg: Message) -> None:
    file = await bot.get_file(msg.document.file_id)
    file_path: str = file.file_path
    await bot.download_file(file_path, 'books/' + msg.document.file_name)



def scan_the_book(file_name: str) -> str:
    try:
        with open('books/' + file_name, encoding='windows-1251') as f:
            return f.read()
    except UnicodeDecodeError:
            with (open('books/' + file_name, encoding='UTF-8')) as f:
                return f.read()


def read_the_book(book_itself):
    return book_itself[:1000]