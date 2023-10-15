from typing import Annotated, Union

from readyapi import ReadyApi, Header

app = ReadyApi()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[
        Union[str, None], Header(convert_underscores=False)
    ] = None
):
    return {"strange_header": strange_header}
