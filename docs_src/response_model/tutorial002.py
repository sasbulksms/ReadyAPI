from typing import Union

from readyapi import ReadyApi
from pydantic import BaseModel, EmailStr

app = ReadyApi()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
