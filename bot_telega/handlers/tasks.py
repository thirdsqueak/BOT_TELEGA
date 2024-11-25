from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import add_task, list_tasks, delete_task

router = Router()

# Словарь для отслеживания состояния пользователей
user_states = {}

@router.message(Command("add"))
async def add_task_start(message: Message):
    user_states[message.from_user.id] = "awaiting_task"
    await message.answer("Введите текст задачи, которую хотите добавить:")

@router.message(lambda message: message.from_user.id in user_states and user_states[message.from_user.id] == "awaiting_task")
async def add_task_finish(message: Message):
    task = message.text.strip()
    if not task:
        await message.answer("Задача не может быть пустой. Пожалуйста, введите текст задачи.")
        return

    add_task(message.from_user.id, task)
    user_states.pop(message.from_user.id, None)  # Сбрасываем состояние пользователя
    await message.answer(f"Задача '{task}' успешно добавлена!")

@router.message(Command("list"))
async def list_tasks_command(message: Message):
    user_tasks = list_tasks(message.from_user.id)
    if not user_tasks:
        await message.answer("Ваш список задач пуст.")
        return

    tasks_list = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(user_tasks)])
    await message.answer(f"Ваши задачи:\n{tasks_list}")

@router.message(Command("delete"))
async def delete_task_start(message: Message):
    user_states[message.from_user.id] = "awaiting_task_number"
    await message.answer("Введите номер задачи, которую хотите удалить:")

@router.message(lambda message: message.from_user.id in user_states and user_states[message.from_user.id] == "awaiting_task_number")
async def delete_task_finish(message: Message):
    try:
        task_index = int(message.text.strip()) - 1
    except ValueError:
        await message.answer("Введите корректный номер задачи.")
        return

    if delete_task(message.from_user.id, task_index):
        user_states.pop(message.from_user.id, None)  # Сбрасываем состояние пользователя
        await message.answer(f"Задача под номером {task_index + 1} удалена.")
    else:
        await message.answer("Задача с таким номером не найдена. Проверьте список задач и попробуйте снова.")
