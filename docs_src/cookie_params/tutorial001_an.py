from typing import Union

from readyapi import Cookie, ReadyApi
from typing_extensions import Annotated

app = ReadyApi()


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}
