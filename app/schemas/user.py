from typing import Literal

from pydantic import ConfigDict, BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    role: Literal["user", "admin"]


class User(UserBase):
    id: int
    role: str
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None
