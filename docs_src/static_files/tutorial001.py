from readyapi import ReadyApi
from readyapi.staticfiles import StaticFiles

app = ReadyApi()

app.mount("/static", StaticFiles(directory="static"), name="static")
