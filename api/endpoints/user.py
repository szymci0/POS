from fastapi import APIRouter, Depends, Response, Request
from api.app import app
from models.user import Users, jwt_authentication
from dependencies.user import create_users_app


def register_routes(fastapi_app):
    fast_api_users = create_users_app()

    fastapi_app.include_router(
        fast_api_users.get_auth_router(jwt_authentication),
        prefix="/auth/jwt",
        tags=['auth'],
    )
    fastapi_app.include_router(
        fast_api_users.get_register_router(),
        prefix="/auth",
        tags=["auth"],
        dependencies=[Depends(app.users.current_user(superuser=True))]
    )
    fastapi_app.include_router(
        fast_api_users.get_verify_router('c8ece35c-8c3b-4ce5-9f32-46ac5a83a234'),
        prefix="/auth", 
        tags=["auth"],
    )
    fastapi_app.include_router(
        fast_api_users.get_users_router(),
        prefix="/users", 
        tags=["users"],
    )

    
    auth_router = APIRouter(prefix="/auth/jwt", tags=["auth"])

    @auth_router.post("/refresh")
    async def refresh_jwt(
        response: Response,
        user=Depends(fast_api_users.get_current_active_user),
    ):
        return await jwt_authentication.get_login_response(user, response)
    
    @auth_router.post("/logout")
    async def logout_user(
            token: str,
    ):
        from models.blacklisted_tokens import BlacklistedTokens
        BlacklistedTokens(token=token).save()

    fastapi_app.include_router(router)
    fastapi_app.include_router(auth_router)


router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    dependencies=[Depends(app.users.current_user(active=True))],
)

@router.get("/")
async def list_users(request: Request):
    return list[Users.objects()]

