from readyapi import ReadyApi

app = ReadyApi(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
