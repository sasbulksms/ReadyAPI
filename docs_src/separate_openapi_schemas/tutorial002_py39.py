from typing import Optional

from pydantic import BaseModel
from readyapi import ReadyAPI


class Item(BaseModel):
    name: str
    description: Optional[str] = None


app = ReadyAPI(separate_input_output_schemas=False)


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
