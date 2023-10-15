from typing import Annotated

from readyapi import ReadyApi, Header

app = ReadyApi()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
):
    return {"strange_header": strange_header}
