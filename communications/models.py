from django.db import models
from account.models import Account
from sprinkler.models import Sprinkler
from pipe.models import Pipe

class Squirt(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey(Sprinkler)
    pipe=models.ForeignKey(Pipe)
    content=models.TextField()
    messageType=models.TextField()


class Spray(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey(Sprinkler)
    pipe=models.ForeignKey(Pipe)
    content=models.TextField()
    messageType=models.TextField()
    sent=models.BooleanField(default=False)

class Load(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    account=models.ForeignKey(Account)
    sprinkler=models.ForeignKey(Sprinkler, related_name="foreign sprinkler")
    pipe=models.ForeignKey(Pipe)
    fromPhone=models.TextField()
    amount=models.FloatField()
