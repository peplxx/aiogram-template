from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from app.data.config import get_settings

settings = get_settings()

default: DefaultBotProperties = DefaultBotProperties(parse_mode=settings.PARSE_MODE)
bot: Bot = Bot(token=settings.BOT_TOKEN, default=default)
storage = MemoryStorage()
dp: Dispatcher = Dispatcher(storage=storage)

