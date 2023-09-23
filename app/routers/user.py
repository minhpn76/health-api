from fastapi import APIRouter, HTTPException
from services.user import get_user_by_id
from db.user import *

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_users():
    list_user = []
    for user in fake_users_db:
        list_user.append({
            "id": user['id'],
            "username": user['username'],
            "email": user['email'],
            "full_name": user['full_name'],
            "disabled": user['disabled']
        })
    return list_user


@router.get("/{user_id}")
async def get_user(user_id: str):
    user = get_user_by_id(fake_users_db, int(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    del user.hashed_password
    return user


@router.put(
    "/{user_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_user(user_id: str):
    if user_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"user_id": user_id, "name": "The great Plumbus"}
