from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexica.lexica import START, HELP, Bookshelve


# Создание переменных и присвоение им значений
router = Router()
bookk = []
forward = InlineKeyboardButton(text='>>', callback_data='forward')
pages = InlineKeyboardButton(text=':)')
back = InlineKeyboardButton(text='<<', callback_data='back')
mu_mu = InlineKeyboardButton(text='Mу-МУ', callback_data='mu-mu')
matrena = InlineKeyboardButton(text='Матренин двор', callback_data='matrena')
moving_keyboard = InlineKeyboardMarkup(inline_keyboard=[[forward], [pages], [back]])
books_keyboard = InlineKeyboardMarkup(inline_keyboard=[[mu_mu], [matrena]])

state = {
    'x': 250
}


def book():
    f = open('MU-MU.txt')
    ff = f
    return ff.read(250)


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


# Реакция на "вперед
@router.callback_query(Text(text=['forward']))
async def forward(callback: CallbackQuery):
    await callback.message.edit_text(book(), reply_markup=moving_keyboard)



