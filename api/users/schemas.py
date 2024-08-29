import pydantic


class SchemaUser(pydantic.BaseModel):
    username: str


class CreateUser(SchemaUser):
    password: str


class AuthUser(CreateUser):
    ...


class GetUser(SchemaUser):
    user_id: int
