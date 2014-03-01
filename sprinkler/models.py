from django.db import models
from pipe.models import Pipe
from account.models import Account, Country

class Sprinkler(models.Model):
    phoneNumber=models.TextField()
    heartbeat=models.DateTimeField(auto_now=True)
    authorized=models.BooleanField(default=False)
    country=models.ForeignKey(Country, default=1)

    def __str__(self):
        if self.authorized:
            authorizedString="authorized"
        else:
            authorizedString="not authorized"
        return "%s %s in %s, last reported in at %s.  Sprinkler is %s" % (self.country.countryCode, self.phoneNumber, self.country, self.heartbeat, authorizedString)

class Squirt(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey(Sprinkler)
    origin=models.ForeignKey(Pipe)
    content=models.TextField()
    read=models.BooleanField(default=False)

class Spray(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    sprinkler=models.ForeignKey(Sprinkler)
    destination=models.ForeignKey(Pipe)
    content=models.TextField()
    messageType=models.TextField()
    sent=models.BooleanField(default=False)

    def __str__(self):
        return "From %s %s to %s at %s:  %s" % (self.sprinkler.country.countryCode, self.sprinkler.phoneNumber, self.destination, self.timeStamp, self.content)


class Load(models.Model):
    timeStamp=models.DateTimeField(auto_now=True)
    account=models.ForeignKey(Account)
    loadPIN=models.TextField()
    sprinkler=models.ForeignKey(Sprinkler, related_name="foreign sprinkler")
    destination=models.ForeignKey(Pipe)
    amount=models.FloatField(default=100)
    sent=models.BooleanField(default=False)
