from aiogram.filters import BaseFilter
from aiogram.types import Message


class FormatFile(BaseFilter):
    async def __call__(self, msg: Message):
        return msg.document.file_name[-3:] =='txt'