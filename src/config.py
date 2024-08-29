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


class JWTConfig(pydantic.BaseModel):
    private_key: str
    public_key: str


class Config(pydantic.BaseModel):
    database_config: DataBaseConfig
    jwt_config: JWTConfig


def get_config(filename: str):
    with open(filename, mode='r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return Config(
        database_config=DataBaseConfig(
            **data['db']
        ),
        jwt_config=JWTConfig(
            **data['jwt']
        )
    )


config = get_config(BASE_DIR + '/' + 'config.yml')
