from fastapi import APIRouter
from .user import router as user_router
from .original_video import router as original_video_router
from .cropped_video import router as cropped_video_router
router = APIRouter()
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(original_video_router, prefix="/original_video", tags=["original_video"])
router.include_router(cropped_video_router, prefix="/cropped_video", tags=["cropped_video"])


