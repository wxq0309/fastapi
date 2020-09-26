from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.models.db import create_connection, disconnect
from app.api.api_v1.api import api_router


def generate_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.debug = True

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_connection)
    application.add_event_handler("shutdown", disconnect)

    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application


app = generate_application()