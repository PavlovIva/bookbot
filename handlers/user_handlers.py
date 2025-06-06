from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from funcs.work_with_book import scan_the_book, download_book, read_the_book
from funcs.filtres import FormatFile
from lexicon.lexica import help_msg
from keyboards.menu import  menu_board
from keyboards.page_change import page_board
from config.data import book_page



router = Router()
book = ''
book_name = ''

@router.message(Command(commands='start'))
async def process_start(msg: Message):
    await msg.reply('Still working on...', reply_markup=menu_board)


@router.message(Command(commands='/help'))
async def give_help(msg: Message):
    await msg.reply(help_msg)


@router.message(F.document, FormatFile())
async def doc_handler(msg: Message):
    global book, book_name
    await download_book(msg)
    book_name = msg.document.file_name
    book = scan_the_book(msg.document.file_name)
    await msg.reply(read_the_book(book), reply_markup=page_board)


@router.callback_query(F.data == 'next')
async def next_page(clb: CallbackQuery):
    book_page[book_name] += 1
    await clb.message.edit_text(read_the_book(book, book_page[book_name]), reply_markup=page_board)


@router.callback_query(F.data == 'back')
async def back_page(clb: CallbackQuery):
    book_page[book_name] -= 1
    await clb.message.edit_text(read_the_book(book, book_page[book_name]), reply_markup=page_board)

@router.message()
async def wrong_move(msg: Message):
    await msg.answer('Wrong!!')