from readyapi import ReadyApi

app = ReadyApi()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
