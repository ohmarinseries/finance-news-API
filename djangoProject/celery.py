import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'collect-articles-every-minute': {
        'task': 'financeAPI.tasks.collect_articles',
        'schedule': crontab(),
    }
}

app.autodiscover_tasks()


