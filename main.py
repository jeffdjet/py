from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    firstname: str
    lastname: str
    gender: str
    age: int

    class Config:
        orm_mode = True


data: List[User] = [
    User(
        firstname="jeff",
        lastname="givera",
        gender="M",
        age=18)
]


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/api/v1/users")
async def fetch_users():
    return data

@app.post("/api/v1/users")
async def add_user(user: User):
    data.append(user)

    return {
        "status" : "SUCCESS",
        "data" : user
    }
