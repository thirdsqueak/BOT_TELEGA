from aiogram import Dispatcher
from .start import router as start_router
from .tasks import router as tasks_router

def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(tasks_router)
