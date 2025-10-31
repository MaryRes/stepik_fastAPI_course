from dataclasses import dataclass

from environs import Env


@dataclass
class DataBaseConfig:
    database_url: str


class Config:
    db: DataBaseConfig
    secret_key: str
    debug: bool


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)  # Загружаем переменные окружения из файла .env

    return Config(
        db=DataBaseConfig(database_url=env("DATABASE_URL")),
        secret_key=env("SECRET_KEY"),
        debug=env.bool("DEBUG", default=False),
    )


config = load_config()
