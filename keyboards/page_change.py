from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

page_btn1 = InlineKeyboardButton(
    text='<<',
    callback_data='back'
)

page_btn2 = InlineKeyboardButton(
    text='>>',
    callback_data='next'
)



page_board = InlineKeyboardMarkup(
    inline_keyboard=[[page_btn1], [page_btn2]]
)