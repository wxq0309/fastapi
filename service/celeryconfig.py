BROKER_URL = "redis://localhost"
# CELERY_RESULT_BACKEND = "redis://localhost"
CELERY_RESULT_BACKEND = "elasticsearch://"

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_ENABLE_UTC = True

# python -m celeryconfig 测试文件是否配置正确
# celery 4.x 版本无法在 win 10 运行 ,其中celery 3.x 与python 3.7版本冲突
# pip install --upgrade https://github.com/celery/celery/tarball/master

# CELERY_ROUTES = {
#     'tasks.add': 'low-priority',
# }
