from functools import lru_cache
from typing import Annotated

from readyapi import Depends, ReadyApi

from .config import Settings

app = ReadyApi()


@lru_cache()
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
