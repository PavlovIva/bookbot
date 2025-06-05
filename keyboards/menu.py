from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexica import menu_buttons


buttons: list[InlineKeyboardButton] = []

for item in menu_buttons:
    buttons.append(InlineKeyboardButton(
        text=item,
        callback_data=item
    ))

menu_board: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[buttons]
)