import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    # Авторизация - ID пользователей, которым разрешено использовать бота
    ALLOWED_USER_IDS = [int(id.strip()) for id in os.getenv('ALLOWED_USER_IDS', '').split(',') if id.strip().isdigit()]
    
    # Todoist
    TODOIST_TOKEN = os.getenv('TODOIST_TOKEN')
    TODOIST_PROJECT_NAME = os.getenv('TODOIST_PROJECT_NAME', 'Inbox')
    
    # OpenAI
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_ASSISTANT_ID = os.getenv('OPENAI_ASSISTANT_ID')
    
    # Настройки
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'ERROR')
    
    @classmethod
    def validate(cls):
        required = ['TELEGRAM_TOKEN', 'TODOIST_TOKEN']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Отсутствуют переменные: {missing}")
            
        if not cls.ALLOWED_USER_IDS:
            raise ValueError("ALLOWED_USER_IDS не настроен - бот будет доступен всем!")
            
        return True

config = Config()