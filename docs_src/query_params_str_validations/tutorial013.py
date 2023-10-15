from readyapi import ReadyApi, Query

app = ReadyApi()


@app.get("/items/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items
