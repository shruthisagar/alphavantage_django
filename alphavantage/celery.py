from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alphavantage.settings")

app = Celery("alphavantage")
app.conf.enable_utc = True

app.conf.beat_schedule = {
    "fetch_and_save": {
        "task": "alpha.tasks.get_latest_and_update_alphavantage",
        "schedule": crontab(hour="*", minute=38),
    }
}

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: ", str(self.request))
