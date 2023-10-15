from readyapi import ReadyApi

app = ReadyApi()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
