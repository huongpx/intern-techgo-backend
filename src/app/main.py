from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .api.api_v1.api import api_router
from .core.config import settings
from .db.base_model import Base

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
)

app.include_router(api_router)
