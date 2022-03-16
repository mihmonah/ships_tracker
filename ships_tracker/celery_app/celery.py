import os

from celery.app import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ships_tracker.settings.settings')

app = Celery()
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'update-every-night': {
        'task': 'ships.tasks.nightly_upload',
        'schedule': crontab(minute=0, hour=0),
    },
}