from enum import Enum
from pydantic import BaseModel,AnyHttpUrl, EmailStr
from typing import Optional
from db.db import db



class CroppedVideo(BaseModel):
    unique_id : str
    video_url : str
    video_name : str
    date_of_event : str
    type_of_event : str
    event_location : str
    uploaded_by : str

    @classmethod
    async def insert_video(cls,video : "CroppedVideo")->None:
        db.collection("cropped_videos").add(video.dict())
    @classmethod
    async def get_video(cls,uid : str)->Optional["CroppedVideo"]:
        doc = db.collection("cropped_videos").where("unique_id", "==", uid).get()
        if len(doc):
            return cls(**doc[0].to_dict())
        else:
            return None