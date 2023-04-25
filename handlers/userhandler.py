from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexica.lexica import START, HELP, Bookshelve


bookss = ['books/MU-MU.txt', 'books/GARDEN.txt']

def page():
    data = {}
    for i in bookss:
        with open(i) as f:
            pgs = len(f.read()) // 500
            data[i] = pgs
    return data


# Создание переменных и присвоение им значений
router = Router()
reading_book: str
kb_builder = InlineKeyboardBuilder()
pg = {}
forward = InlineKeyboardButton(text='>>', callback_data='forward')
pagess = InlineKeyboardButton(text='page', callback_data='yes')
back = InlineKeyboardButton(text='<<', callback_data='back')
mu_mu = InlineKeyboardButton(text='Mу-МУ', callback_data='books/MU-MU.txt')
garden = InlineKeyboardButton(text='Матренин двор', callback_data='books/GARDEN.txt')
books_keyboard = InlineKeyboardMarkup(inline_keyboard=[[mu_mu], [garden]])
moving_keyboard = kb_builder.row(back, pagess, forward, width=3)
state = {}


def book(path: str):
    with open(path) as f:
        pg = f.read()
        return pg[state[reading_book]['x']:state[reading_book]['y']]


# Реакция на "старт"
@router.message(Command(commands='start'))
async def start(msg: types.Message):
    await msg.reply(START)


# Реакция на "помощь"
@router.message(Command(commands='help'))
async def help(msg: types.Message):
    await msg.reply(HELP)


# Реакция на "полка"
@router.message(Command(commands='shelve'))
async def shelve(msg: types.Message):
    await msg.reply(Bookshelve, reply_markup=books_keyboard)


@router.callback_query(Text(text='forward'))
async def forward(callback: CallbackQuery):
    global pg
    state[reading_book]['x'] += 500
    state[reading_book]['y'] += 500
    pg[reading_book] += 1
    await callback.message.edit_text(f'{book(reading_book)}', reply_markup=moving_keyboard.as_markup())


@router.callback_query(Text(text='back'))
async def back(callback: CallbackQuery):
    global pg
    state[reading_book]['x'] -= 500
    state[reading_book]['y'] -= 500
    pg[reading_book] -= 1
    await callback.message.edit_text(f'{book(reading_book)}', reply_markup=moving_keyboard.as_markup())


@router.callback_query(Text(text='yes'))
async def show_pages(callback: CallbackQuery):
    await callback.answer(f'{str(pg[reading_book])}/{str(page()[reading_book])}')


@router.callback_query()
async def mu_mu(callback: CallbackQuery):
    global reading_book, pg
    reading_book = callback.data
    pg[reading_book] = 1
    state[reading_book] = {'x': 0,
                           'y': 500}
    await callback.message.edit_text(f'{book(callback.data)}', reply_markup=moving_keyboard.as_markup())
