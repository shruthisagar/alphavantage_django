from celery import shared_task
from celery.schedules import crontab
from .controllers import store_latest_data


@shared_task
def get_latest_and_update_alphavantage():
    store_latest_data()
