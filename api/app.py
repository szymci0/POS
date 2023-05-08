from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api.mongodb import connect_db, close_db
from jwt import jwt_middleware, security_headers_middleware
from endpoints import user
app = FastAPI()

app.include_router(user.router)

def init_app():
    app = FastAPI()
    connect_db()
    app.add_event_handler("shutdown", close_db)
    app.middleware("http")(security_headers_middleware)
    app.middleware("http")(jwt_middleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
        allow_credentials=True,
    )

@app.on_event("startup")
def register_routes():
    from endpoints import (
        user,
    )

    user.register_routes(app)

    app.include_router(user.router)


def run_dev_server():
    uvicorn.run(
        app="api.app:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    )

if __name__ == "__main__":
    run_dev_server()
