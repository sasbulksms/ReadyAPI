from readyapi import ReadyAPI
from readyapi.responses import ORJSONResponse
from readyapi.testclient import TestClient
from sqlalchemy.sql.elements import quoted_name

app = ReadyAPI(default_response_class=ORJSONResponse)


@app.get("/orjson_non_str_keys")
def get_orjson_non_str_keys():
    key = quoted_name(value="msg", quote=False)
    return {key: "Hello World", 1: 1}


client = TestClient(app)


def test_orjson_non_str_keys():
    with client:
        response = client.get("/orjson_non_str_keys")
    assert response.json() == {"msg": "Hello World", "1": 1}
