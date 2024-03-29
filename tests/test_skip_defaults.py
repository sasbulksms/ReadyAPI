from typing import Optional

from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.testclient import TestClient

app = ReadyAPI()


class SubModel(BaseModel):
    a: Optional[str] = "foo"


class Model(BaseModel):
    x: Optional[int] = None
    sub: SubModel


class ModelSubclass(Model):
    y: int
    z: int = 0
    w: Optional[int] = None


class ModelDefaults(BaseModel):
    w: Optional[str] = None
    x: Optional[str] = None
    y: str = "y"
    z: str = "z"


@app.get("/", response_model=Model, response_model_exclude_unset=True)
def get_root() -> ModelSubclass:
    return ModelSubclass(sub={}, y=1, z=0)


@app.get(
    "/exclude_unset", response_model=ModelDefaults, response_model_exclude_unset=True
)
def get_exclude_unset() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")


@app.get(
    "/exclude_defaults",
    response_model=ModelDefaults,
    response_model_exclude_defaults=True,
)
def get_exclude_defaults() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")


@app.get(
    "/exclude_none", response_model=ModelDefaults, response_model_exclude_none=True
)
def get_exclude_none() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")


@app.get(
    "/exclude_unset_none",
    response_model=ModelDefaults,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def get_exclude_unset_none() -> ModelDefaults:
    return ModelDefaults(x=None, y="y")


client = TestClient(app)


def test_return_defaults():
    response = client.get("/")
    assert response.json() == {"sub": {}}


def test_return_exclude_unset():
    response = client.get("/exclude_unset")
    assert response.json() == {"x": None, "y": "y"}


def test_return_exclude_defaults():
    response = client.get("/exclude_defaults")
    assert response.json() == {}


def test_return_exclude_none():
    response = client.get("/exclude_none")
    assert response.json() == {"y": "y", "z": "z"}


def test_return_exclude_unset_none():
    response = client.get("/exclude_unset_none")
    assert response.json() == {"y": "y"}
