from aiogram import Bot
from aiogram.types import Message
from config.config import load_config
from config.data import book_page

config = load_config()
bot: Bot = Bot(token=config.tg_bot.token)


async def download_book(msg: Message) -> None:
    file = await bot.get_file(msg.document.file_id)
    file_path: str = file.file_path
    await bot.download_file(file_path, 'books/' + msg.document.file_name)
    book_page[msg.document.file_name] = 1




def scan_the_book(file_name: str) -> str:
    try:
        with open('books/' + file_name, encoding='windows-1251') as f:
            return f.read()
    except UnicodeDecodeError:
            with (open('books/' + file_name, encoding='UTF-8')) as f:
                return f.read()


def read_the_book(book_itself, page=1):
    return book_itself[page * 500 - 500: page * 500]


