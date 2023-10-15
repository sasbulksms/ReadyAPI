from readyapi import ReadyApi
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"


settings = Settings()

app = ReadyApi(openapi_url=settings.openapi_url)


@app.get("/")
def root():
    return {"message": "Hello World"}
