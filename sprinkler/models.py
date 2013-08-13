from django.db import models
from country.models import Country

class Sprinkler(models.Model):
    ipAddress=models.TextField()
    localIpAddress=models.TextField()
    heartbeat=models.DateTimeField(auto_now=True)
    load=models.FloatField()
    sprinklerCountry=models.ForeignKey(Country)

    def __str__(self):
        return "local IP:  %s    remote IP:  %s   last heartbeat:  %s  country:  %s" %(self.localIpAddress, self.ipAddress, self.heartbeat, self.sprinklerCountry.name)
