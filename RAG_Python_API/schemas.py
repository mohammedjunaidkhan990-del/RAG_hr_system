from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    password: str
    department: Optional[str] = None

class AuthResponse(BaseModel):
    token: str
    username: str
    user_id: int

class UserCreate(BaseModel):
    username: str
    password: str
    department: Optional[str] = None
    roles: str = "ROLE_USER"

class Token(BaseModel):
    access_token: str
    token_type: str