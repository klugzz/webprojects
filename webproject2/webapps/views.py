from django.shortcuts import render
def index(request):
	return render(request,'apps/inde.html')
def home(request):
	return render(request,'apps/home.html')
def service(request):
	return render(request,'apps/services.html')
def gallery(request):
	return render(request,'apps/gallery.html')
def contact(request):
	return render(request,'apps/contact.html')
# Create your views here.
