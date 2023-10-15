from readyapi import ReadyApi
from readyapi.responses import UJSONResponse

app = ReadyApi()


@app.get("/items/", response_class=UJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]
