from celery import Celery

from . import celeryconfig
from .config import settings

app = Celery(settings.CELERY_NAME)

app.config_from_object(celeryconfig)
