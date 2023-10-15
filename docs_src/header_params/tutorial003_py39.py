from typing import Union

from readyapi import ReadyApi, Header

app = ReadyApi()


@app.get("/items/")
async def read_items(x_token: Union[list[str], None] = Header(default=None)):
    return {"X-Token values": x_token}
