from readyapi import ReadyApi
from readyapi.middleware.cors import CORSMiddleware

app = ReadyApi()

origins = [
    "http://localhost.khulnasoft.com",
    "https://localhost.khulnasoft.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
