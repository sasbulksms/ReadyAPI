from readyapi import ReadyApi
from readyapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = ReadyApi()


@app.get("/")
async def main():
    return FileResponse(some_file_path)
