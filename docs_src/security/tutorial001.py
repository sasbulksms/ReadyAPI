from readyapi import Depends, ReadyApi
from readyapi.security import OAuth2PasswordBearer

app = ReadyApi()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
