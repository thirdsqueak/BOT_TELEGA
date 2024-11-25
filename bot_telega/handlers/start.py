
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я Дневник бот. Используй команды для работы с задачами:\n"
                         "/add - Добавить задачу\n"
                         "/list - Показать все задачи\n"
                         "/delete - Удалить задачу")
