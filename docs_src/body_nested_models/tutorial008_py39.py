from readyapi import ReadyApi
from pydantic import BaseModel, HttpUrl

app = ReadyApi()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images
