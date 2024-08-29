import bcrypt

from api.users.schemas import AuthUser
from src.models import User


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )


def auth_user(user: User, user_schema: AuthUser) -> bool:
    return validate_password(user_schema.password, user.password)
