from readyapi import ReadyApi
from readyapi.responses import ORJSONResponse

app = ReadyApi(default_response_class=ORJSONResponse)


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]
