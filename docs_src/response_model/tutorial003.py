from typing import Any, Union

from readyapi import ReadyApi
from pydantic import BaseModel, EmailStr

app = ReadyApi()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
