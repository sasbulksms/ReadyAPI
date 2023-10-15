from typing import Annotated

from readyapi import ReadyApi, Query
from pydantic import Required

app = ReadyApi()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
