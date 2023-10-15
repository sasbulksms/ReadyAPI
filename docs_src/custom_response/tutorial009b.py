from readyapi import ReadyApi
from readyapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = ReadyApi()


@app.get("/", response_class=FileResponse)
async def main():
    return some_file_path
