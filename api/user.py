from typing import Optional
from fastapi import APIRouter
from models.users import User
from models.login_form import login
from models.original_videos import VideoOriginal
from models.cropped_videos import CroppedVideo
from fastapi import Depends, APIRouter, status, UploadFile, HTTPException
import uuid
import hashlib

router = APIRouter()

def hash_password(password: str)->str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


@router.post("/create_user", response_model=User)
async def create_user(user_details:User)->Optional[User]:
    user_details.unique_id = str(uuid.uuid4().hex)
    user_details.password = hash_password(user_details.password)
    is_existing = await User.get_user_by_email(user_details.email)
    if is_existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists.",
        )
    else:
        user = await User.insert_user(user=user_details)
    return user

@router.get("/get_user/{uid}", response_model=User)
async def get_user(uid: str)->Optional[User]:
    user = await User.get_user(uid=uid)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

@router.post("/login_user", response_model=User)
async def login_user(login_details:login)->Optional[User]:
    user = await User.get_user_by_email(email=login_details.email)
    password_g = hash_password(login_details.password)
    if user:
        if password_g == user.password:
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password.",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User does not exist.",
        )

@router.put("/update_user/{uid}", response_model=User)
async def update_user(uid: str, user_details:User)->Optional[User]:
    user = await User.get_user(uid=uid)
    if user:
        user.email = user_details.email
        user.password = user_details.password
        user.device1 = user_details.device1
        user.device2 = user_details.device2
        user.share_perm = user_details.share_perm
        user.upload_perm = user_details.upload_perm
        user.access_level = user_details.access_level
        user = await User.update_user(uid=uid,user=user)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

@router.get("/get_all_users", response_model=User)
async def get_all_users()->list:
    users = await User.get_all_users()
    return users