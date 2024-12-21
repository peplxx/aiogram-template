from aiogram.types import Message

from app.loader import dp


@dp.message()
async def unknown_message(message: Message):
    await message.answer("Я не могу распознать ваше сообщение.")

