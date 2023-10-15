from readyapi import ReadyApi
from readyapi.responses import ORJSONResponse

app = ReadyApi()


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])
