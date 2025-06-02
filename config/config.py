from dataclasses import dataclass
from environs import Env

@dataclass
class Tgbot:
    token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: Tgbot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=Tgbot(
            token=env('bot_token'),
            admin_id=env('admin_id')
        )
    )
