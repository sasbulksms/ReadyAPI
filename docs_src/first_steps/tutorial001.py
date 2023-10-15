from readyapi import ReadyApi

app = ReadyApi()


@app.get("/")
async def root():
    return {"message": "Hello World"}
