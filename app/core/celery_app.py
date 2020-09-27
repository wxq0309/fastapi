from celery import Celery

from . import celeryconfig
from .config import settings

celery_app = Celery(settings.CELERY_NAME)

celery_app.config_from_object(celeryconfig)
