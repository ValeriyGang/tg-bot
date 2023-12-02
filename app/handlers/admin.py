from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

class admin:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        pass