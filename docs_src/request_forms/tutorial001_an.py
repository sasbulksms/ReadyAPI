from readyapi import ReadyApi, Form
from typing_extensions import Annotated

app = ReadyApi()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
