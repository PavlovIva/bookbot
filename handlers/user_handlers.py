from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()



@router.message(CommandStart)
async def prosecc_start(msg: Message):
    await msg.reply('Still working on...')
