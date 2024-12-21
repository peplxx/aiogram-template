from aiogram.filters import Command
from aiogram.types import Message

from app.handlers import __modules__
from app.loader import dp, bot
from logging import getLogger

log = getLogger(__name__)


# /ping
@dp.message(Command(commands=["ping"]))
async def ping(message: Message):
    await message.reply("Pong!")


def log_initialized_modules(modules: list = __modules__):
    log.info(f"Initialized modules: {[module.__name__ for module in modules]}")


# Entry point
if __name__ == '__main__':
    log_initialized_modules()

    dp.run_polling(bot)
