from typing import List
from fastapi import APIRouter, status, Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from dependencies.db import conn
from schemas.user import User, userEntity, usersEntity

user = APIRouter()

@user.get('/users',response_model=List[User], tags=["Users"])
async def find_all_users():
    return usersEntity(conn.local.user.find())


@user.post('/users', response_model=User, tags=["Users"])
async def create_new_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)


@user.get('/users/{id}', response_model=User, tags=["Users"])
async def find_single_user(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}", response_model=User, tags=["Users"])
async def update_user(id: str, user: User):

    updated_user = dict(user)
    updated_user["password"] = sha256_crypt.encrypt(updated_user["password"])

    conn.local.user.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(updated_user)
    })
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
async def delete_user(id: str):
    conn.local.user.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
