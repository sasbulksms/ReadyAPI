from readyapi import ReadyApi
from readyapi.responses import RedirectResponse

app = ReadyApi()


@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"
