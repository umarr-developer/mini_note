import os

import pydantic
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class DataBaseConfig(pydantic.BaseModel):
    database: str
    host: str
    user: str
    password: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.database}"



class Config(pydantic.BaseModel):
    database_config: DataBaseConfig


def get_config(filename: str):
    with open(filename, mode='r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return Config(
        database_config=DataBaseConfig(
            **data['db']
        )
    )


config = get_config(BASE_DIR + '/' + 'config.yml')
