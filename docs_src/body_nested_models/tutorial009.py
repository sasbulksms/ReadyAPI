from typing import Dict

from readyapi import ReadyApi

app = ReadyApi()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
