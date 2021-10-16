from datetime import datetime
from django.db import models


class AlphavantageBTCtoUSD(models.Model):
    id = models.AutoField(primary_key=True)
    exchange_rate = models.FloatField()
    last_refresh_time = models.DateTimeField()
    created_time = models.DateTimeField(default=datetime.utcnow)
