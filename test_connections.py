import asyncio
from src.config import config
from todoist_api_python.api import TodoistAPI

async def test_connections():
    print("🔧 Тестируем подключения...")
    
    # Проверяем конфигурацию
    try:
        config.validate()
        print("✅ Конфигурация корректна")
    except Exception as e:
        print(f"❌ Ошибка конфигурации: {e}")
        return
    
    # Тестируем Todoist
    try:
        api = TodoistAPI(config.TODOIST_TOKEN)
        projects = api.get_projects()     
        print(f"✅ Todoist подключен. Найдено проектов: {len(projects)}")

    except Exception as e:
        print(f"❌ Ошибка Todoist: {e}")
        import traceback
        traceback.print_exc()
    
    print("🎉 Тест завершен!")

if __name__ == "__main__":
    asyncio.run(test_connections())