from typing import Dict, List, Optional, Tuple

import pytest
from pydantic import BaseModel
from readyapi import Query, ReadyAPI


def test_invalid_sequence():
    with pytest.raises(AssertionError):
        app = ReadyAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: List[Item] = Query(default=None)):
            pass  # pragma: no cover


def test_invalid_tuple():
    with pytest.raises(AssertionError):
        app = ReadyAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Tuple[Item, Item] = Query(default=None)):
            pass  # pragma: no cover


def test_invalid_dict():
    with pytest.raises(AssertionError):
        app = ReadyAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Dict[str, Item] = Query(default=None)):
            pass  # pragma: no cover


def test_invalid_simple_dict():
    with pytest.raises(AssertionError):
        app = ReadyAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Optional[dict] = Query(default=None)):
            pass  # pragma: no cover
