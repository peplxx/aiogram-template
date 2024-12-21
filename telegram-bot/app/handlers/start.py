import json
from typing import Optional, get_args
from uuid import UUID

from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from httpx import Response
from pydantic import BaseModel
from starlette import status

from app.data.db.models import User
from app.loader import dp, bot


class StartArgs(BaseModel):
    # All members should be Optional
    uuid: Optional[UUID] = None


def get_actual_type(field_type):
    return get_args(field_type)[0]


def parse_start_arguments(start_message: Message) -> StartArgs:
    text = start_message.text
    split = text.split(" ")
    possible_args = [] if len(split) == 1 else split[1:]
    accepting_args = StartArgs().dict()
    args_keys = list(accepting_args.keys())
    for argument in possible_args:
        try:
            key, value = argument.split('=')
            if key in args_keys:
                arg_info = StartArgs().__fields__[key]
                arg_type = get_actual_type(arg_info.annotation)
                accepting_args[key] = arg_type(value)
        finally:
            continue
    return StartArgs(**accepting_args)

