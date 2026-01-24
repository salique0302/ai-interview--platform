from datetime import datetime, timedelta
from typing import Dict
from uuid import uuid4

from jose import jwt, JWTError

# These should come from environment variables in production
SECRET_KEY = "super-secret-key-change-this"
ALGORITHM = "HS256"

ISSUER = "ai-interview-platform"
AUDIENCE = "ai-interview-api"

ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_access_token(
    subject: str,
    email: str,
    role: str,
    token_version: int,
) -> str:
    now = datetime.utcnow()
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload: Dict = {
        "sub": subject,
        "email": email,
        "role": role,
        "jti": str(uuid4()),
        "token_version": token_version,
        "iat": int(now.timestamp()),
        "exp": int(expire.timestamp()),
        "iss": ISSUER,
        "aud": AUDIENCE,
    }

    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str) -> Dict:
    try:
        decoded = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            audience=AUDIENCE,
            issuer=ISSUER,
        )
        return decoded
    except JWTError:
        return None
