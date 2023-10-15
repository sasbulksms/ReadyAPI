from readyapi import ReadyApi

from . import a, b

app = ReadyApi()

app.include_router(a.router, prefix="/a")
app.include_router(b.router, prefix="/b")
