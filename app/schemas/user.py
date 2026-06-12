import uuid
from pydantic import BaseModel, EmailStr
from app.models.user import Plan


class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    plan: Plan
    is_active: bool

    model_config = {"from_attributes": True}
