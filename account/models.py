from django.db import models
from country.models import Country

class Account(models.Model):
    userCountry=models.ForeignKey(Country)
    value=models.FloatField()
    name=models.TextField()
    address=models.TextField()    
    province=models.TextField()
    phoneNumber=models.TextField()
