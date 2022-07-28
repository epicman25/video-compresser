from enum import Enum
from pydantic import BaseModel,AnyHttpUrl, EmailStr
from typing import Optional
from db.db import db


    

class VideoOriginal(BaseModel):
    unique_id : str
    video_url : str
    video_name : str
    date_of_event : str
    type_of_event : str
    event_location : str
    uploaded_by : str
 
    @classmethod
    async def insert_video(cls,video : "VideoOriginal")->None:
        db.collection("original_videos").add(video.dict())

    @classmethod
    async def get_video(cls,uid : str)->Optional["VideoOriginal"]:
        doc = db.collection("original_videos").where("unique_id", "==", uid).get()
        if len(doc):
            return cls(**doc[0].to_dict())
        else:
            return None

