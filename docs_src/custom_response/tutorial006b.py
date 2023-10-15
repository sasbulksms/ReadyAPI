from readyapi import ReadyApi
from readyapi.responses import RedirectResponse

app = ReadyApi()


@app.get("/readyapi", response_class=RedirectResponse)
async def redirect_readyapi():
    return "https://readyapi.khulnasoft.com"
