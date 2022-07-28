from enum import Enum
import imp
from xmlrpc.client import Boolean
from pydantic import BaseModel,AnyHttpUrl, EmailStr
from typing import Optional

from requests import delete
from db.db import db
    


class User(BaseModel):
    unique_id : str
    email : EmailStr
    password : str
    device1 : str
    device2 : str
    share_perm : Boolean = False
    upload_perm : Boolean = False
    access_level : int = 2

    @classmethod
    async def insert_user(cls,user : "User")->None:
        user = user.dict()
        db.collection("users").add(user)


    @classmethod
    async def get_user(cls,uid : str)->Optional["User"]:
        doc = db.collection("users").where("unique_id", "==", uid).get()
        if len(doc):
            return cls(**doc[0].to_dict())
        else:
            return None

    @classmethod
    async def get_user_by_email(cls,email : EmailStr)->Optional["User"]:
        doc = db.collection("users").where("email", "==", email).get()
        if len(doc):
            return cls(**doc[0].to_dict())   
        return False



    @classmethod
    async def delete_user(cls,uid : str)->None:
        doc = db.collection("users").where("unique_id", "==", uid).get()
        if len(doc):
            db.collection("users").document(doc[0].id).delete()

    @classmethod
    async def update_user(cls,uid : str,user : "User")->Optional["User"]:
        doc = db.collection("users").where("unique_id", "==", uid).get()
        if len(doc):
            db.collection("users").document(doc[0].id).update(user.dict())
            return cls(**doc[0].to_dict())
        else:
            return None

    @classmethod
    async def get_all_users(cls)->list:
        doc = db.collection("users").get()
        return [cls(**i[0].to_dict()) for i in doc]
        
        


    

