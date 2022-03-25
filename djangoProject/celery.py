import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {

}

app.autodiscover_tasks()


@app.task()
def task_test(self):
    pass
