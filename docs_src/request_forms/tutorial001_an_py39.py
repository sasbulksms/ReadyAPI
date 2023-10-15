from typing import Annotated

from readyapi import ReadyApi, Form

app = ReadyApi()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
