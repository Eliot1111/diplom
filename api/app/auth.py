"""Password hashing and JWT creation."""

import os
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash


SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "diploma-demo-change-this-secret-before-production",
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Hash a plaintext password for storage."""
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against its stored hash."""
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(username: str) -> str:
    """Create a signed, expiring access token for a username."""
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        {"sub": username, "exp": expires_at},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
