from django.db import models

class Country(models.Model):
    name=models.TextField()
    textRate=models.FloatField(blank=True, null=True)
    abbreviation=models.TextField(blank=True)
    countryCode=models.TextField()
    currencyCode=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    country=models.ForeignKey(Country)
    value=models.FloatField()
    name=models.TextField()
    address=models.TextField()    
    province=models.TextField()
    phoneNumber=models.TextField()

    def __str__(self):
        return self.name

