from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  

import datetime
from device.models import AreaDevice

def index(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

def lista(request):
	dev = AreaDevice.objects.all()
	attr = "==>".join([dev[0].name, dev[0].description, dev[0].manufacturer])
	return render (request, 'device.html', {'title': "prob" , 'ad': dev[0].__dict__})
