from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


router = Router()

forward = InlineKeyboardButton(text='>>', callback_data='forward')
back = InlineKeyboardButton(text='<<', callback_data='back')
keyboard = InlineKeyboardMarkup(inline_keyboard=[[forward], [back]])

position = 0
def book(position):
    f = open('book1.txt')
    position = f.tell()
    return position


@router.message(Command(commands='start'))
async def start(msg: types.Message):
    f = open('book1.txt')
    try:
        await msg.reply(f.read(250), reply_markup=keyboard)
    except:
        pass


@router.callback_query(Text(text=['forward']))
async def forward(callback: CallbackQuery):
    await callback.message.edit_text(str(book(position)), reply_markup=keyboard)
