from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	print('This line printed by view function whilw processing request')
	return HttpResponse('<h1>APPLICATION RUNNING SUCCESSFULLY</h1>')
# Create your views here.
