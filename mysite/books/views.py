from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book 

def search_form(request):
	return render(request,'book/search_form.html')

def search(request):
	error = False
	if 'q' in request.GET and request.GET['q']:
		#message = 'we received ' + request.GET['q']
		books = Book.objects.filter(title__icontains=request.GET['q'])
		return render(request,'book/search_result.html',{'books':books,'query':request.GET['q']})
		message = books
	else:
		#message = 'nothing we received'
		error = True
		return render(request,'book/search_form.html',{'error':error})

	return HttpResponse(message)