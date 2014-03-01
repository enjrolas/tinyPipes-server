from django.db import models
from account.models import Account
from sprinkler.models import Sprinkler
from pipe.models import Pipe

class Squirt(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey(Sprinkler)
    origin=models.ForeignKey(Pipe)
    content=models.TextField()
    messageType=models.TextField()
    read=models.BooleanField(blank=True)

class Spray(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey(Sprinkler)
    destination=models.ForeignKey(Pipe)
    content=models.TextField()
    messageType=models.TextField()
    sent=models.BooleanField(default=False)

    def __str__(self):
        return "From %s to %s at %s:  %s" % (self.sprinkler.name, self.destination, self.timeStamp, self.content)


class Load(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    account=models.ForeignKey(Account)
    loadPIN=models.TextField()
    sprinkler=models.ForeignKey(Sprinkler, related_name="foreign sprinkler")
    destination=models.ForeignKey(Pipe)
    amount=models.FloatField(default=100)
    sent=models.BooleanField(default=False)    
