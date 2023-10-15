from typing import List

from readyapi import ReadyApi, Query

app = ReadyApi()


@app.get("/items/")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items
