from django.db import models
from account.models import Account
from sprinkler.models import Sprinkler

class Pipe(models.Model):
    serialNumber=models.IntegerField()
    version=models.TextField()
    phoneNumber=models.TextField()
    lattitude=models.FloatField()
    longitude=models.FloatField()
    sprinkler=models.ForeignKey(Sprinkler)
    status=models.TextField()
    batteryHealth=models.IntegerField()
    panelHealth=models.IntegerField()
    batteryCapacity=models.IntegerField()
    pipeLoad=models.FloatField()
    account=models.ForeignKey(Account)
    billingRate=models.FloatField()
    billingType=models.TextField()
    billingPeriod=models.DateTimeField()
