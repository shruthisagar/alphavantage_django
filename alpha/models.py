from django.db import models

class AlphavantageData(models.Model):
    open_value = models.FloatField()
    low_value = models.FloatField()
    close_value = models.FloatField()
    high_value = models.FloatField()
    created_time = models.DateTimeField()
    volume_value = models.IntegerField()