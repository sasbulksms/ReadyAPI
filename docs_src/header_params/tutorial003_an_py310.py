from typing import Annotated

from readyapi import ReadyApi, Header

app = ReadyApi()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
