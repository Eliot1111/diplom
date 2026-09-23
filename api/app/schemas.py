"""Request and response schemas for the API."""

from pydantic import BaseModel, ConfigDict


class LoginRequest(BaseModel):
    """Credentials supplied when logging in."""
    username: str
    password: str


class Token(BaseModel):
    """An access token and its authorization scheme."""
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    """Public user details, excluding the password hash."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    role: str


class ItemCreate(BaseModel):
    """Fields accepted when creating an item."""
    name: str
    description: str | None = None


class ItemResponse(ItemCreate):
    """Stored item details returned by the API."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_id: int
