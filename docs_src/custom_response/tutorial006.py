from readyapi import ReadyApi
from readyapi.responses import RedirectResponse

app = ReadyApi()


@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")
