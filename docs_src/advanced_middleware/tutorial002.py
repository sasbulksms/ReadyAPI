from readyapi import ReadyApi
from readyapi.middleware.trustedhost import TrustedHostMiddleware

app = ReadyApi()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
