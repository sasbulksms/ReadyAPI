from functools import lru_cache

from readyapi import Depends, ReadyApi
from typing_extensions import Annotated

from . import config

app = ReadyApi()


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
