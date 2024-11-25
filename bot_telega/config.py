from pydantic_settings import BaseSettings  # Импорт из нового пакета

class Config(BaseSettings):
    BOT_TOKEN: str  = '7867953635:AAGu0lNynHiXN7jGo-B4IAiceQFguW-QlMU'

    class Config:
        env_file = ".env"  # Файл для переменных окружения


config = Config()
