from celery import Celery

app = Celery('qiang01_celery')
app.config_from_object('qiang01_celery.tasks.config')
# 让celery找到任务
app.autodiscover_tasks('qiang01_celery.tasks.sms')

