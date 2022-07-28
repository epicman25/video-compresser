from enum import Enum
import imp
from pydantic import BaseModel,AnyHttpUrl, EmailStr
from typing import Optional
from db.db import db



class login(BaseModel):
    email : EmailStr
    password : str
    

    

