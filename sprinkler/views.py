from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from django.shortcuts import render_to_response
import os
from sprinkler.models import Sprinkler
from country.models import Country
import urllib

def heartbeat(request,ip):
    publicIp=get_client_ip(request)
    try:
        rainbird=Sprinkler.objects.get(ipAddress=publicIp)        
        rainbird.localIpAddress=ip
        rainbird.save()
    except:
        URL = "http://api.hostip.info/get_html.php?ip=%s&position=true" %publicIp
        response=urllib.urlopen(URL).read()
        lines=response.split('\n')        
        if len(lines)>0:
            country=lines[0].split(':')[1]
            try:
                sprinklerCountry=Country.objects.get(name=country)
            except DoesNotExist:
                sprinklerCountry=Country(name=country, textRate=0)
                sprinklerCountry.save()
            rainbird=Sprinkler(ipAddress=publicIp, localIpAddress=ip, load=0,sprinklerCountry=sprinklerCountry)
            rainbird.save()
    return render_to_response("heartbeat.html", {"ipAddress":ip})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def sprinklers(request):
    rainbirds=Sprinkler.objects.all()
    return render_to_response("sprinklers.html", {"sprinklers":rainbirds})

