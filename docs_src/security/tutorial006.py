from readyapi import Depends, ReadyApi
from readyapi.security import HTTPBasic, HTTPBasicCredentials

app = ReadyApi()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
