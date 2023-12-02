from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.DataBase.bd import check, reg_user_id

from app.keyboards.user_menu import menu
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Добро пожаловать! {message.from_user.full_name}', reply_markup=menu())
    
    if check(message.from_user.id):
        await message.answer("Вы уже зарегистрированы")
    else:
        reg_user_id(message.from_user.id, message.from_user.first_name) # здесь закончил, нужно проверить пользователя, есть ли он в бд

@router.message() # Обработчик ВСЕХ сообщений от пользователей
async def text(message: Message):
    if message.text != "Бот":
        await message.answer(f"Я не знаю, что на это ответить")
    else:
        await message.answer(f"Да, это я!")

        