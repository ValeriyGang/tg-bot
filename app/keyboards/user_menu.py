from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def menu() -> ReplyKeyboardMarkup: # Вызов главного меню
    kb = ReplyKeyboardBuilder()
    kb.button(text="Статус")
    kb.button(text="Профиль")
    kb.button(text="Подписка")
    kb.adjust(1)
    return kb.as_markup()