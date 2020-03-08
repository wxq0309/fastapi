from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from dao.db import create_connection, disconnect
from controller.api.ihou import router as iehou_router
from controller.api.ulink import router as ulink_router
from controller.api.user import router as user_router


def generate_application() -> FastAPI:
    application = FastAPI()
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

    application.include_router(
        iehou_router,
        prefix="/iehou",
        tags=["iehou"]
    )

    application.include_router(
        ulink_router,
        prefix="/ulink",
        tags=["ulink"]
    )

    application.include_router(
        user_router,
        prefix="/user",
        tags=["users"]
    )

    return application


app = generate_application()