from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers
from ServerScript.models import ChatPoint
import json

# Create your views here.
def parse(request, name):
	if name == 'setChat':
		x_ = request.GET['x']
		y_ = request.GET['y']
		chat_name_ = request.GET['chat_name']
		query = ChatPoint(chat_name = chat_name_, x=x_, y=y_)
		query.save()
		return HttpResponse("OK")
	else:
		return HttpResponse("lalka")

def print_array(request):
	return HttpResponse(serializers.serialize("json", ChatPoint.objects.all()))

def map_with_points(request):
	if 'chat_name' in request.POST:
		if float(request.POST['y']) not in list(map(lambda x: float(x.y), ChatPoint.objects.all())) and float(request.POST['x']) not in list(map(lambda x: float(x.x), ChatPoint.objects.all())):
			x = str(request.POST['x'])
			y = str(request.POST['y'])
			messages = str(request.POST['message']) + '<br> '
			chat_name = request.POST['chat_name']
			ChatPoint(chat_name = chat_name, x=x, y=y, messages=messages).save()
	elif 'message' in request.POST:
		x = str(request.POST['x'])
		y = str(request.POST['y'])
		chat = ChatPoint.objects.get(x=x, y=y)
		chat.messages += request.POST['message'] + '<br> '
		chat.save()

	else:
		print(request.GET)
	points = list(map(lambda z: [z.x, z.y, z.chat_name, z.messages], ChatPoint.objects.all()))	
	return render(request, 'map.htm', {'points' : points})

