from django.db import models
from django.forms import ModelForm

class Squirt(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey('sprinkler.Sprinkler')
    pipe=models.ForeignKey('pipe.Pipe')
    content=models.TextField()
    messageType=models.TextField()


class Spray(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey('sprinkler.Sprinkler')
    pipe=models.ForeignKey('pipe.Pipe')
    content=models.TextField()
    messageType=models.TextField()
    sent=models.BooleanField(default=False)

class Load(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    account=models.ForeignKey('account.Account')
    sprinkler=models.ForeignKey('sprinkler.Sprinkler')
    pipe=models.ForeignKey('pipe.Pipe')
    fromPhone=models.TextField()
    amount=models.FloatField()
