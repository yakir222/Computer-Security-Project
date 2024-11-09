from typing import Optional
from pydantic import BaseModel, EmailStr

import computersecuritydb.database_manager as dbm

class UserCreateBody(BaseModel):
    username: str
    password: str
    email: EmailStr
class User(UserCreateBody):
    requires_pass_change: bool = 0

class UpdatePasswordBody(BaseModel):
    username: str
    new_password: str
    old_password: str

class UserLoginBody(BaseModel):
    username: str
    password: str

class UserResetPasswordBody(BaseModel):
    email: EmailStr

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    requires_pass_change: bool = 0
