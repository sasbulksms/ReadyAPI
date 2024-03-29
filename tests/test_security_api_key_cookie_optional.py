from typing import Optional

from pydantic import BaseModel
from readyapi import Depends, ReadyAPI, Security
from readyapi.security import APIKeyCookie
from readyapi.testclient import TestClient

app = ReadyAPI()

api_key = APIKeyCookie(name="key", auto_error=False)


class User(BaseModel):
    username: str


def get_current_user(oauth_header: Optional[str] = Security(api_key)):
    if oauth_header is None:
        return None
    user = User(username=oauth_header)
    return user


@app.get("/users/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    if current_user is None:
        return {"msg": "Create an account first"}
    else:
        return current_user


def test_security_api_key():
    client = TestClient(app, cookies={"key": "secret"})
    response = client.get("/users/me")
    assert response.status_code == 200, response.text
    assert response.json() == {"username": "secret"}


def test_security_api_key_no_key():
    client = TestClient(app)
    response = client.get("/users/me")
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Create an account first"}


def test_openapi_schema():
    client = TestClient(app)
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/users/me": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Current User",
                    "operationId": "read_current_user_users_me_get",
                    "security": [{"APIKeyCookie": []}],
                }
            }
        },
        "components": {
            "securitySchemes": {
                "APIKeyCookie": {"type": "apiKey", "name": "key", "in": "cookie"}
            }
        },
    }
