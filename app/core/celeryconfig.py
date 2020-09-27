from kombu import Queue

from app.core.config import settings

BROKER_URL = settings.BROKER_URL
CELERY_RESULT_BACKEND = settings.CELERY_RESULT_BACKEND

CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_ENABLE_UTC = True
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

CELERY_QUEUES = (  # 设置add队列,绑定routing_key
    Queue('default', routing_key='default'),
    Queue('email', routing_key='send_email'),
)

CELERY_ROUTES = {  # projq.tasks.add这个任务进去add队列并routeing_key为xue.add
    'app.api.api_v1.tasks.emails.decoratorEmail': {
        'queue': 'email',
        'routing_key': 'send_email',
    }
}
