from aiogram.types import Message, ContentType

from app.loader import dp


@dp.message(lambda message: message.content_type == ContentType.STICKER)
async def get_sticker_id(message: Message):
    await message.reply(f"Sticker ID: {message.sticker.file_id}")