from typing import Union

from readyapi import ReadyApi, Query
from typing_extensions import Annotated

app = ReadyApi()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
