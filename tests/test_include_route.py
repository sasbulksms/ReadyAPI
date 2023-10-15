from readyapi import APIRouter, ReadyApi, Request
from readyapi.responses import JSONResponse
from readyapi.testclient import TestClient

app = ReadyApi()
router = APIRouter()


@router.route("/items/")
def read_items(request: Request):
    return JSONResponse({"hello": "world"})


app.include_router(router)

client = TestClient(app)


def test_sub_router():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == {"hello": "world"}
