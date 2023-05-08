from motor.motor_asyncio import AsyncIOMotorClient

client = {"mongodb": None}


def get_db_client() -> AsyncIOMotorClient:
    return client["mongodb"]


def connect_db():
    client["mongodb"] = AsyncIOMotorClient(
        "mongodb://localhost:27017/pos-project",
        uuidRepresentation="standard",
    )

async def close_db():
    client["mongodb"].close()
