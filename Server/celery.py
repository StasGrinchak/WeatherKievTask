import os
from celery.schedules import crontab
from celery import Celery
import django
django.setup()
from Weather.models import ParserSetting


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")

app = Celery("Server")
app.config_from_object("django.conf:settings", namespace="CELERY")

#getting update time from database
instance_time = ParserSetting.objects.first()
time = str(instance_time.update_time).split(':')

#crontab for task execution
app.conf.beat_schedule = {
    'parse-weather-kiev': {
        'task': 'Server.tasks.parser',
        'schedule': crontab(hour=time[0], minute=time[1]),
    }
}

app.autodiscover_tasks()