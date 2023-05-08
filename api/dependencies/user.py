from typing import Tuple

from fastapi_users import FastAPIUsers
from fastapi_users.db import MongoDBUserDataBase

from models.user import (
    User,
    UserCreate,
    UserDB,
    UserUpdate,
    jwt_authentication
)

from mongodb import get_db_client


def create_users_app():
    mongo_client = get_db_client()
    db = mongo_client["pos-project"]
    collection = db["users"]
    user_db = MongoDBUserDataBase(UserDB, collection)

    fastapi_users = FastAPIUsers(
        user_db, [jwt_authentication], User, UserCreate, UserUpdate, UserDB,
    )
    fastapi_users.collection = collection
    return fastapi_users