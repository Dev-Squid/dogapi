from datetime import datetime
from pydantic import BaseModel, EmailStr, Json
from typing import Optional

class UserRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    created_at: datetime

class DogBase(BaseModel):
    name: str
    characteristics: Optional[Json] = None

class DogRequest(DogBase):
    pass

class DogResponse(DogBase):
    user_id: int
    user: UserResponse

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None 

class CommentRequest(BaseModel):
    content: str
    dog_id: int

class CommentResponse(BaseModel):
    content: str
    created_at: datetime

    class Config:
        orm_mode = True

class VoteRequest(BaseModel):
    comment_id: int

class VoteResponse(BaseModel):
    comment_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
    