from fastapi import Response
from bson import ObjectId
from fastapi_users import models
from fastapi_users.models import BaseUserDB
from mongoengine import DynamicDocument, UUIDField
from fastapi_users.authentication import JWTAuthentication
from pydantic import validator
from typing import Optional, Any
from abc import ABC
from api.app import app
from datetime import datetime


class User(models.BaseUser):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    created_at: Optional[datetime] = None
    last_seen: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    
    @validator("created_at", pre=True, always=True)
    def default_created_at(cls, v):
        return v or datetime.now()


class UserCreate(models.BaseUserCreate):
    @validator("password")
    def valid_password(cls, v: str):
        if len(v) < 4:
            raise ValueError("Password too short(<4)")
        return v


class UserDB(models.BaseOAuthAccountMixin, User, models.BaseUserDB):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class Users(DynamicDocument):
    id = UUIDField()
    meta = {
        'id_field': 'id',
    }


class CustomJWTAuthentication(JWTAuthentication, ABC):
    async def get_login_response(
            self, user: BaseUserDB, response: Response,
    ) -> Any:
        user.last_seen = datetime.now()
        await app.users.db.update(user)
        login_response = await super().get_login_response(user, response)
        return login_response
    

DAY = 60 * 60 * 24
jwt_authentication = CustomJWTAuthentication(
    secret='c8ece35c-8c3b-4ce5-9f32-46ac5a83a234', lifetime_seconds=DAY, tokenUrl="/auth/jwt/login"
)
