from readyapi import ReadyApi, status

app = ReadyApi()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
