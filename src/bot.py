"""
Telegram-Todoist Bot - основной файл
"""

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from config import config


# Настройка логирования
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Инициализация бота
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()


async def check_auth(message: Message) -> bool:
    """Проверить авторизацию пользователя"""
    user_id = message.from_user.id if message.from_user else None
    allowed_ids = config.ALLOWED_USER_IDS
    
    if not user_id or user_id not in allowed_ids:
        logger.warning(f"Неавторизованная попытка доступа от пользователя {user_id}")
        await message.answer(
            "❌ У вас нет доступа к этому боту.\n"
        )
        return False
    
    return True


@dp.message(Command("start"))
async def start_handler(message: Message):
    """Обработчик команды /start"""
    if not await check_auth(message):
        return
    
    await message.answer(
        "🎯 *Telegram-Todoist Bot*\n\n"
        "Привет! Я помогу создавать задачи в Todoist из пересланных сообщений.\n\n"
        "Просто пересылай мне любые сообщения - я превращу их в задачи! 📝",
        parse_mode="Markdown"
    )


async def main():
    """Запуск бота"""
    try:
        # Проверяем конфигурацию
        config.validate()
        logger.info("Конфигурация валидна")
        
        # Запускаем бота
        logger.info("Запуск бота...")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())