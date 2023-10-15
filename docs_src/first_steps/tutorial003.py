from readyapi import ReadyApi

app = ReadyApi()


@app.get("/")
def root():
    return {"message": "Hello World"}
