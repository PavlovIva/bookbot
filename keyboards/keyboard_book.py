from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

buttons: list[InlineKeyboardButton] = []

for item in os.listdir(path='/home/jon/PycharmProjects/bookbot/books'):
    btn: InlineKeyboardButton = InlineKeyboardButton(
        text=item,
        callback_data='pressed'
    )
    buttons.append(btn)


book_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[buttons]
)
