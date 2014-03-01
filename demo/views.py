from django.shortcuts import render
from datetime import datetime, timedelta 
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from django.shortcuts import render_to_response
import os
from demo.models import Measurement, DemoPanel
from django.views.decorators.csrf import csrf_exempt
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def demo(request):
    return render_to_response("demo/demo.html")

@csrf_exempt
def measurement(request, voltage="0", current="0", enabled="0"):    
    panel=DemoPanel.objects.get()
    measurement=Measurement()
    measurement.current=float(current)
    measurement.voltage=float(voltage)
    measurement.enabled=bool(enabled)
    measurement.energy=measurement.current*measurement.voltage
    measurement.save()    
    panel=DemoPanel.objects.get()
    return render_to_response("demo/demoData.html", {"panel":panel})

@csrf_exempt
def energy(request):
    dataPoints=Measurement.objects.filter(timeStamp__gte=datetime.now()-timedelta(minutes=5)).order_by('timeStamp')[:50]
    #dataPoints=Measurement.objects.order_by('timeStamp')[:50]
#    dataPoints=Measurement.objects.filter(timeStamp__gte=datetime.now()-timedelta(minutes=10)).order_by('timeStamp')[:50]
    return render_to_response("demo/tinyEnergy.json", {"data":dataPoints})

@csrf_exempt
def voltage(request):
    dataPoints=Measurement.objects.filter(timeStamp__gte=datetime.now()-timedelta(minutes=5)).order_by('timeStamp')[:50]
    return render_to_response("demo/tinyVoltage.json", {"data":dataPoints})


@csrf_exempt
def demoControl(request, enabled="true"):
    logger.error('Something went wrong!')
    panel=DemoPanel.objects.get()
    logger.error(panel)
    response=request.POST['enabled']
    if request.POST.get("enabled","")=="true":
        panel.enabled=True
    else:
        panel.enabled=False
    panel.save()
    return render_to_response("demo/demoData.html", {"panel":panel, "response":response})

