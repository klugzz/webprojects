from django.shortcuts import render
from django.http import HttpResponse
def testing(request):
	a=30
	b=50
	c=a+b
	x=x='<h1> A value is....' + str(a) + 'B value id...'+ str(b) + 'SUM value is...'+str(c)+'</h1>'
	return HttpResponse

# Create your views here.
