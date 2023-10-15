from typing import Union

from readyapi import ReadyApi, Header

app = ReadyApi()


@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}
