from readyapi import ReadyApi
from readyapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = ReadyApi()

app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def main():
    return {"message": "Hello World"}
