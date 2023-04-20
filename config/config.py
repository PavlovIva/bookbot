from environs import Env
from dataclasses import dataclass

@dataclass
class Tgbot:
    token: str


@dataclass
class Config:
    tg_bot: Tgbot


def load_config():
    env = Env()
    env.read_env()
    return Config(tg_bot=Tgbot(token=env('TOKEN')))


