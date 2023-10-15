from readyapi import ReadyApi

my_awesome_api = ReadyApi()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}
