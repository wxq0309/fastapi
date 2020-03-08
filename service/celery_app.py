from celery import Celery

from . import celeryconfig

# 直接配置
# app = Celery(
#     "fast_worker",
#     broker="redis://localhost",
#     backend="redis://localhost"
# )
# app.conf.CELERY_TASK_SERIALIZER = "json"

# 推荐使用配置模块 celeryconfig
app = Celery("fastapi_worker")

app.config_from_object(celeryconfig)

