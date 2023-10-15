from dataclasses import dataclass
from typing import Union

from readyapi import ReadyApi


@dataclass
class Item:
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None


app = ReadyApi()


@app.post("/items/")
async def create_item(item: Item):
    return item
