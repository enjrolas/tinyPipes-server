from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from sprinkler.models import Squirt, Spray, Sprinkler
from pipe.models import Pipe
import os
import datetime

def home(request):
    return render(request, 'control/home.html')

def sprinklers(request):
    sprinklers=Sprinkler.objects.filter(heartbeat__gt=(datetime.datetime.now()-datetime.timedelta(minutes=1)))  # get all sprinklers that have been active in the last minute        
    return render(request, "control/sprinklers.html", {"sprinklers":sprinklers})

def accounts(request):
    pipes=Pipe.objects.all().exclude(account__name__contains = "Solar Love")
    return render(request, "control/accounts.html", {"pipes":pipes})

def logs(request):
    squirts=Squirt.objects.all().order_by('-timeStamp')
    sprays=Spray.objects.all().order_by('-timeStamp')
    return render(request, 'control/logs.html', {"sprays":sprays, "squirts": squirts})

def command(request):
    pipeId=int(request.POST.get("pipe"))
    action=request.POST.get("command")
    if action=="enable":
        enable(pipeId)
        return HttpResponse("enabling")
    if action=="disable":
       disable(pipeId)
    if action=="Collect Measurements":
        spray(pipeId,"status") 
    if action=="Instantaneous Measurement":
        spray(pipeId,"instantaneous") 
    return HttpResponse("ok")

def texttext(request):
    return render_to_response("control/texttext.html")

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

#this creates a Spray (communication from the sprinkler to the pipe) object and saves it in 
#the database.  The sprinkler will find it next time it polls, and send it out the pipe
def spray(pipeId, message):
    destination=Pipe.objects.get(pk=pipeId)
    sprinkler=Sprinkler.objects.filter(country=destination.country).first()
    spray=Spray(sprinkler=sprinkler, 
                destination=destination,
                content=message,
                messageType="action",
                sent=False)
    spray.save()

def enable(pipeId):
    spray(pipeId, "connect")
    destination=Pipe.objects.get(pk=pipeId)
    destination.status="enabled"
    destination.save()

def disable(pipeId):
    spray(pipeId, "disconnect")
    destination=Pipe.objects.get(pk=pipeId)
    destination.status="disabled"
    destination.save()
