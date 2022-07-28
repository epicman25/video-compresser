from typing import Optional
from fastapi import APIRouter
from models.users import User
from models.original_videos import VideoOriginal
from models.cropped_videos import CroppedVideo
from fastapi import Depends, APIRouter, status, UploadFile, HTTPException
import uuid


router = APIRouter()

@router.post("/upload_video", response_model=VideoOriginal)
async def upload_video(video_details: VideoOriginal):
    video_details.unique_id = str(uuid.uuid4().hex)
    is_existing = await VideoOriginal.get_video(uid=video_details.unique_id)
    if is_existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Video already exists.",
        )
    else:
        video = await VideoOriginal.insert_video(video=video_details)
        return video

@router.get("/get_video/{uid}", response_model=VideoOriginal)
async def get_video(uid: str)->Optional[VideoOriginal]:
    video = await VideoOriginal.get_video(uid=uid)
    if video:
        return video
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video does not exist.",
        )