import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    
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
        return True

config = Config()