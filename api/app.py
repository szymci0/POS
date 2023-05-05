from fastapi import FastAPI
from endpoints import user
from api.config import init_database()
app = FastAPI()

app.include_router(user.router)

@app.on_event("startup")
async def start_database():
    await init_database()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
