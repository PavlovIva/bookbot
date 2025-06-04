from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command
from config.config import  load_config
from funcs.work_with_book import read_the_book
from funcs.filtres import FormatFile
from lexicon.lexica import help_msg


config = load_config()

bot = Bot(token=config.tg_bot.token)
router = Router()


@router.message(Command(commands='start'))
async def process_start(msg: Message):
    await msg.reply('Still working on...')


@router.message(Command(commands='/help'))
async def give_help(msg: Message):
    await msg.reply(help_msg)


@router.message(F.document, FormatFile())
async def doc_handler(msg: Message):
    file = await bot.get_file(msg.document.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, msg.document.file_name)
    read_the_book(msg.document.file_name)


@router.message()
async def wrong_move(msg: Message):
    await msg.answer('Wrong!!')