from django.db import models

class Measurement(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    current=models.FloatField()
    enabled=models.BooleanField()
    voltage=models.FloatField()
    energy=models.FloatField()

class DemoPanel(models.Model):
    enabled=models.BooleanField(default=True)
