from django.shortcuts import render, render_to_response
import datetime 
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
import os
from sprinkler.models import Sprinkler, Squirt, Spray, Load
from account.models import Country
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def heartbeat(request):
    phoneNumber=request.POST.get('phoneNumber')
    if phoneNumber is None:
        phoneNumber="5555555555"
    sprinkler, created=Sprinkler.objects.get_or_create(phoneNumber=phoneNumber)
    sprinkler.save()    
    return HttpResponse("ok")
                           
def texttext(request):
    return render_to_response("texttext.html")

def sendtext(request):
    number=request.POST.get("number","")
    content=request.POST.get("content","")
    spray=Spray(sprinkler=destination.sprinkler, 
                destination=0,
                content=message,
                messageType="misc",
                phoneNumber=" ",
                sent=False)
    spray.save()
    return HttpResponse("ok")

@csrf_exempt
def getSpray(request, phoneNumber):
    sprinkler=Sprinkler.objects.get(phoneNumber=phoneNumber)
    sprinkler.save()
    spray=Spray.objects.filter(sprinkler=sprinkler).filter(sent=False).first()
    return render(request, "sprinkler/spray.html", {"spray":spray})

@csrf_exempt
def addSquirt(request):
    from_=request.POST.get("From")
    origin=request.POST.get("Origin")
    content=request.POST.get("Body")
    pipe=Pipe.objects.get(phoneNumber=origin)
    sprinkler=Sprinkler.objects.get(phoneNumber=from_)
    squirt=Squirt(sprinkler=sprinkler, origin=pipe, content=content)
    
    return HttpResponse("ok")

