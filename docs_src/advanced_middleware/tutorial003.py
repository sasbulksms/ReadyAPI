from readyapi import ReadyApi
from readyapi.middleware.gzip import GZipMiddleware

app = ReadyApi()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/")
async def main():
    return "somebigcontent"
