
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class Profile(BaseModel):
    username: str
    address: str
    email: EmailStr
    avatarURL: str

class ProfileSchema(BaseModel):
    username: str = Field(...)
    address: str = Field(...)
    email: EmailStr = Field(...)
    avatarURL: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "address": "0x12345678",
                "email": "jdoe@x.edu.ng",
                "avatarURL": "https://avatar.io",
            }
        }


class UpdateProfileModel(BaseModel):
    username: Optional[str]
    address: Optional[str]
    email: Optional[EmailStr]
    avatarURL: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "address": "0x12345678",
                "email": "jdoe@x.edu.ng",
                "avatarURL": "https://avatar.io",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}