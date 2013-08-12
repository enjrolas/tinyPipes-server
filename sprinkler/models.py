from django.db import models

class Sprinkler(models.Model):
    ipAddress=models.TextField()
    heartbeat=models.DateTimeField(auto_now=True)
    load=models.FloatField()
    country=models.ForeignField('Country')

class Country(models.Model):
    name=models.TextField()
    textRate=models.FloatField()
    countryCode=models.TextField()
    currencyCode=models.TextField()
