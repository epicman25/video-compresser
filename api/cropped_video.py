from typing import Optional
from fastapi import APIRouter
from models.users import User 
from models.original_videos import VideoOriginal
from models.cropped_videos import CroppedVideo
from fastapi import Depends, APIRouter, status, UploadFile, HTTPException
import uuid

router = APIRouter()

@router.post("/upload_cropped_video", response_model=CroppedVideo)
async def upload_cropped_video(video_details: CroppedVideo)->Optional[CroppedVideo]:
    video_details.unique_id = uuid.uuid4().hex
    is_existing = await CroppedVideo.get_video(uid=video_details.unique_id)
    if is_existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Video already exists.",
        )
    else:
        video = await CroppedVideo.insert_video(video=video_details)
        return video

@router.get("/get_cropped_video/{uid}", response_model=CroppedVideo)
async def get_cropped_video(uid: str)->Optional[CroppedVideo]:
    video = await CroppedVideo.get_video(uid=uid)
    if video:
        return video
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video does not exist.",
        )