from readyapi import ReadyApi
from readyapi.responses import RedirectResponse

app = ReadyApi()


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
