from django.db import models

class Country(models.Model):
    name=models.TextField()
    textRate=models.FloatField()
    countryCode=models.TextField()
    currencyCode=models.TextField()

