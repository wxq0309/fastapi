from kombu import Queue

from app.core.config import settings

broker_url = settings.BROKER_URL
result_backend = settings.CELERY_RESULT_BACKEND

result_serializer = "json"
accept_content = ['json']
timezone = "Asia/Shanghai"
CELERY_enable_utc = True
result_expires = 60 * 60 * 24

task_queues = (  # 设置add队列,绑定routing_key
    Queue('default', routing_key='default'),
    Queue('email', routing_key='send_email'),
)

task_routes = {  # projq.tasks.add这个任务进去add队列并routeing_key为xue.add
    'app.api.api_v1.tasks.emails.decoratorEmail': {
        'queue': 'email',
        'routing_key': 'send_email',
    }
}
