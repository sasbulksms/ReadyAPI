from readyapi import ReadyApi, Query
from typing_extensions import Annotated

app = ReadyApi()


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items
