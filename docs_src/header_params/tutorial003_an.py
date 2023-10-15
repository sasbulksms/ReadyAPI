from typing import List, Union

from readyapi import ReadyApi, Header
from typing_extensions import Annotated

app = ReadyApi()


@app.get("/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}
