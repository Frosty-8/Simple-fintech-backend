from datetime import (
    datetime, timedelta
)

from jose import jwt

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    payload = data.copy()

    expire = (
        datetime.now()
        + timedelta(
            minutes=TOKEN_EXPIRE_MINUTES
        )
    )

    payload["exp"] = expire

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])