import aioredis
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logger import logger
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

    @application.on_event("startup")
    async def create_redis_app():
        application.state.redis = await aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

    @application.on_event("shutdown")
    async def stop_redis_app():
        application.state.redis.close()
        await application.state.redis.wait_close()

    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application


if __name__ == '__main__':
    app = generate_application()
    logger.getlogger().info("app已加载")
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=9000
    )
