from readyapi import ReadyApi
from readyapi.responses import PlainTextResponse

app = ReadyApi()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"
