from readyapi import Cookie, ReadyApi

app = ReadyApi()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
