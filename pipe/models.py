from django.db import models
from account.models import Account, Country

class Pipe(models.Model):
    serialNumber=models.TextField()
    version=models.TextField(default="v2.3", blank=True, null=True)
    phoneNumber=models.TextField(default="", blank=True, null=True)
    country=models.ForeignKey(Country)
    lattitude=models.FloatField(default="14.56", blank=True, null=True)
    longitude=models.FloatField(default="120.99", blank=True, null=True)
    status=models.TextField(default="enabled", blank=True, null=True)
    batteryHealth=models.IntegerField(default=100, blank=True, null=True)
    panelHealth=models.IntegerField(default=100, blank=True, null=True)
    batteryCapacity=models.IntegerField(default=720, blank=True, null=True)
    pipeLoad=models.FloatField(default=100, blank=True, null=True)
    account=models.ForeignKey(Account)
    billingRate=models.FloatField(default=15, blank=True, null=True)
    billingType=models.TextField(default="daily", blank=True, null=True)

    def __str__(self):
        return "%s %s %s" %(self.account.name, self.serialNumber, self.phoneNumber)
