from typing import Optional

from readyapi import ReadyAPI, Security
from readyapi.security import OAuth2PasswordBearer
from readyapi.testclient import TestClient

app = ReadyAPI()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/token",
    description="OAuth2PasswordBearer security scheme",
    auto_error=False,
)


@app.get("/items/")
async def read_items(token: Optional[str] = Security(oauth2_scheme)):
    if token is None:
        return {"msg": "Create an account first"}
    return {"token": token}


client = TestClient(app)


def test_no_token():
    response = client.get("/items")
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Create an account first"}


def test_token():
    response = client.get("/items", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200, response.text
    assert response.json() == {"token": "testtoken"}


def test_incorrect_token():
    response = client.get("/items", headers={"Authorization": "Notexistent testtoken"})
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Create an account first"}


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                    "security": [{"OAuth2PasswordBearer": []}],
                }
            }
        },
        "components": {
            "securitySchemes": {
                "OAuth2PasswordBearer": {
                    "type": "oauth2",
                    "flows": {"password": {"scopes": {}, "tokenUrl": "/token"}},
                    "description": "OAuth2PasswordBearer security scheme",
                }
            }
        },
    }
