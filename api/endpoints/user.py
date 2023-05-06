from schemas import schemas
from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from database import User
import oauth2
from serializers.userSerializers import userResponseEntity

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}