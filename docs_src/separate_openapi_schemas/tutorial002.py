from typing import List, Union

from readyapi import ReadyApi
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None


app = ReadyApi(separate_input_output_schemas=False)


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/items/")
def read_items() -> List[Item]:
    return [
        Item(
            name="Portal Gun",
            description="Device to travel through the multi-rick-verse",
        ),
        Item(name="Plumbus"),
    ]
