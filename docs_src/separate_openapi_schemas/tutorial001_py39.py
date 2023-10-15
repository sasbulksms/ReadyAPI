from typing import Optional

from readyapi import ReadyApi
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None


app = ReadyApi()


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/items/")
def read_items() -> list[Item]:
    return [
        Item(
            name="Portal Gun",
            description="Device to travel through the multi-rick-verse",
        ),
        Item(name="Plumbus"),
    ]
