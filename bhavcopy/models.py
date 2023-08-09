from django.db import models

class Equity(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
