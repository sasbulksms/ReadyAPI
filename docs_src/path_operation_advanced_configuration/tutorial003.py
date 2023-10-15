from readyapi import ReadyApi

app = ReadyApi()


@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "Foo"}]
