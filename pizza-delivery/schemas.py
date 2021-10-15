from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "username": "rickyla",
                "email": "rickyla@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = 'b6fe6044a54485dbd25b39ab44b9973b936cc7239075890121cca647c3b6f22d'

class LoginModel(BaseModel):
    username: str
    password: str