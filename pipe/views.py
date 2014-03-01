from django.shortcuts import render
import datetime 
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from django.shortcuts import render_to_response, render
import os
from pipe.models import Pipe
from sprinkler.models import Sprinkler, Spray, Squirt
from account.models import Country
import urllib
from django.views.decorators.csrf import csrf_exempt

