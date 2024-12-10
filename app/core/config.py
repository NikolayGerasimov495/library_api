from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr

load_dotenv()


class Settings(BaseSettings):
    app_title: str = 'Библиотечный каталог (0.1)'
    description: str = 'Сервис для работы с книгами, авторами и процессом выдачи книг читателям'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
