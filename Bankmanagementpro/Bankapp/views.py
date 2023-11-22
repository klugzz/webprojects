from django.shortcuts import render,redirect
from Bankapp.models import Bank
from Bankapp.forms import BankForm
import csv
from django.http import HttpResponse
def final(request):
	bank=Bank.objects.all()
	return render(request,'apps/final.html',{'b':bank})
def forms(request):
	form=BankForm()
	if request.method=="POST":
		form=BankForm(request.POST)
		if form.is_valid():
			form.save()
		return final(request)
	return render(request,'apps/form.html',{'form':form})
def file(request):
	response=HttpResponse(content_type='text/csv')
	response['content-Disposition']='attachment;filename=account.csv'
	bank=Bank.objects.all()
	writer=csv.writer(response)
	writer.writerow(['ACNO','NAME','DEPAMNT','BAL'])
	for i in bank:
		writer.writerow([i.acno,i.name,i.depamnt,i.bal])
	return response



def read(request):
	bank=Bank.objects.all()
	return render(request,'apps/result.html',{'b':bank})
def insert(request):
	form=BankForm()
	if request.method=="POST":
		form=BankForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	b=Bank.objects.get(id=id)
	b.delete()
	return redirect('/result')
def update(request,id):
	bank=Bank.objects.get(id=id)
	if request.method=="POST":
		form=BankForm(request.POST,instance=bank)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render (request,'apps/update.html',{'b':bank})
# Create your views here.
