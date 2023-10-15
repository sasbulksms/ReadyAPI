from typing import Union

from readyapi import ReadyApi, Header
from typing_extensions import Annotated

app = ReadyApi()


@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}
