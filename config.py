"""Модуль для описания классов конфигурации."""

from dataclasses import dataclass
from os import getenv

from dotenv import find_dotenv, load_dotenv


@dataclass
class App:
    """API для телеграм-приложения."""

    api_id: int
    api_hash: str
    session: str
    system_version: str
    device_model: str


@dataclass
class Ids:
    """IDs для канала-стиллера и каналов-источников."""

    target_id: int
    source_ids: list[int]


@dataclass
class Config:
    """Обобщенный класс конфигурации."""

    app: App
    ids: Ids


def load_config(path: str | None = None) -> Config:
    """Проверяет файл .env."""
    # Проверяет наличие файла .env.
    if not find_dotenv():
        exit('Отсутствует файл .env')

    # Загружает переменные окружения.
    load_dotenv()

    config = Config(
        app=App(
            api_id=int(getenv('api_id')),
            api_hash=getenv('api_hash'),
            session=getenv('session'),
            system_version=getenv('system_version'),
            device_model=getenv('device_model'),
        ),
        ids=Ids(
            target_id=int(getenv('target_id')),
            source_ids=list(map(int, getenv('source_ids').split(', '))),
        ),
    )

    # Проверяет наличие api_id и api_hash в файле .env.
    if None in (config.app.api_id, config.app.api_hash):
        exit('Отсутствуют api_id и/или api_hash в файле .env')

    # Возвращает заполненный экземпляр класса Config.
    return config
