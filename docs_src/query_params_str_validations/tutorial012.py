from typing import List

from readyapi import ReadyAPI, Query

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items
