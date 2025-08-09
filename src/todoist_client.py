"""
Клиент для работы с Todoist API
Создание задач из пересланных сообщений с поддержкой выбора проекта
"""

import logging
from typing import Optional, List, Dict
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Task, Project
from config import config

logger = logging.getLogger(__name__)


class TodoistClient:
    """Клиент для взаимодействия с Todoist API"""
    
    def __init__(self):
        """Инициализация клиента"""
        self.api = TodoistAPI(config.TODOIST_TOKEN)
        self._default_project_id = None
    
    async def get_default_project_id(self) -> str:
        """Получить ID проекта по умолчанию на основе настроек"""
        if self._default_project_id is None:
            try:
                projects = self.api.get_projects()
                target_project_name = config.TODOIST_PROJECT_NAME.lower()
                
                # Ищем проект по названию
                for project in projects:
                    if project.name.lower() == target_project_name:
                        self._default_project_id = project.id
                        logger.info(f"Найден проект: '{project.name}' (ID: {project.id})")
                        return self._default_project_id
                
                # Если не найден - берем Inbox
                for project in projects:
                    if project.name.lower() == 'inbox':
                        self._default_project_id = project.id
                        logger.warning(f"Проект '{config.TODOIST_PROJECT_NAME}' не найден. Используется Inbox")
                        return self._default_project_id
                
                # Если и Inbox нет - берем первый
                if projects:
                    self._default_project_id = projects[0].id
                    logger.warning(f"Используется первый доступный проект: '{projects[0].name}'")
                else:
                    raise ValueError("Нет доступных проектов")
                
            except Exception as e:
                logger.error(f"Ошибка при получении проектов: {e}")
                raise
                
        return self._default_project_id
    
    async def create_task(
        self, 
        title: str, 
        description: str = ""
    ) -> Task:
        """
        Создать задачу в Todoist
        
        Args:
            title: Заголовок задачи (до 500 символов)
            description: Описание задачи (до 16383 символов)
            
        Returns:
            Task: Созданная задача
        """
        try:
            project_id = await self.get_default_project_id()
            
            # Ограничиваем длину заголовка
            if len(title) > 500:
                title = title[:497] + "..."
            
            # Ограничиваем длину описания
            if len(description) > 16383:
                description = description[:16380] + "..."
            
            task = self.api.add_task(
                content=title,
                description=description,
                project_id=project_id
            )
            
            logger.info(f"Задача создана: {task.id} - {title[:50]}...")
            return task
            
        except Exception as e:
            logger.error(f"Ошибка создания задачи: {e}")
            raise
    
    async def create_task_from_message(
        self, 
        message_text: str, 
        author: str = ""
    ) -> Task:
        """
        Создать задачу из пересланного сообщения
        
        Args:
            message_text: Текст сообщения
            author: Автор сообщения  
            
        Returns:
            Task: Созданная задача
        """
        # Простой заголовок
        title = f"Задача от {author}" if author else "Пересланное сообщение"
        
        # Простое описание в формате Markdown
        description = f"**Автор:** {author}\n**Текст сообщения:** {message_text}"
        
        return await self.create_task(title, description)
    
    def test_connection(self) -> bool:
        """Тестировать подключение к Todoist"""
        try:
            self.api.get_projects()
            return True
        except Exception as e:
            logger.error(f"Ошибка подключения к Todoist: {e}")
            return False