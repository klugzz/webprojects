from django.http import HttpResponse
class Testng(object):
	def __init__(self,get_response):
	   self.get_response=get_response

	def __call__(self,request):
		return HttpResponse('<h1>APPLICATION HAS STOPPED</h1>')