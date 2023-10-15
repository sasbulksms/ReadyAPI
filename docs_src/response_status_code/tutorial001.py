from readyapi import ReadyApi

app = ReadyApi()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
