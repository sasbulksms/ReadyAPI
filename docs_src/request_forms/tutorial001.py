from readyapi import ReadyApi, Form

app = ReadyApi()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
