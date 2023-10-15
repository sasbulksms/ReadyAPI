from readyapi import APIRouter, ReadyApi
from readyapi.testclient import TestClient

app = ReadyApi()

router = APIRouter()


@router.get("/users/{id}")
def read_user(segment: str, id: str):
    return {"segment": segment, "id": id}


app.include_router(router, prefix="/{segment}")


client = TestClient(app)


def test_get():
    response = client.get("/seg/users/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"segment": "seg", "id": "foo"}
