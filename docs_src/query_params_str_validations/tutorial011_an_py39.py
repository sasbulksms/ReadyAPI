from typing import Annotated, Union

from readyapi import ReadyApi, Query

app = ReadyApi()


@app.get("/items/")
async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items
