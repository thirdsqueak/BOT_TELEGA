from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import config
from handlers import register_handlers

# Инициализация бота и диспетчера
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# Регистрация обработчиков
register_handlers(dp)

# Настройка команд
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="add", description="Добавить задачу"),
        BotCommand(command="list", description="Показать список задач"),
        BotCommand(command="delete", description="Удалить задачу"),
        BotCommand(command="start", description="Начать работу с ботом")
    ]
    await bot.set_my_commands(commands)

# Запуск бота
async def main():
    print("Бот запущен!")
    await set_commands(bot)  # Установить команды
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

