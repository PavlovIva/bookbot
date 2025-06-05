from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from funcs import read_the_book, download_book
from funcs import FormatFile
from lexicon import help_msg
from keyboards import book_keyboard, menu_board



router = Router()


@router.message(Command(commands='start'))
async def process_start(msg: Message):
    await msg.reply('Still working on...', reply_markup=menu_board)


@router.message(Command(commands='/help'))
async def give_help(msg: Message):
    await msg.reply(help_msg)


@router.message(F.document, FormatFile())
async def doc_handler(msg: Message):
    await download_book(msg)
    await msg.reply(read_the_book(msg.document.file_name), reply_markup=book_keyboard)


@router.message()
async def wrong_move(msg: Message):
    await msg.answer('Wrong!!')