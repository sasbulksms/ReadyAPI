from readyapi import ReadyApi

app = ReadyApi()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = ReadyApi()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
