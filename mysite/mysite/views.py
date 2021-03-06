from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
import datetime
from .forms import ContactForm
from django.core.mail import send_mail, get_connection

def hello(request):
	#print('now',datetime.datetime.now())
	result = request.META
	show_result =''
	for key in result:
		show_result = show_result + '<p>' + key + ":" + str(result[key]) + '<p>'
	return HttpResponse(show_result)

def current_time(request):
	now = datetime.datetime.now()
	t = get_template('current_time.html')
	#result = "<h1>{}</h1>".format(now)
	#result = t.render({'current_date':now})
	#return HttpResponse(result)
	return render(request,'current_time.html',{'current_date': now})

def time_plus(request,plus):
	plus = int(plus)
	
	if plus > 100:
		raise Http404()
	result = datetime.datetime.now() + datetime.timedelta(hours=plus)
	#result=datetime.timedelta(hours=plus)
	return HttpResponse(result)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(cd['subject'],
				      cd['message'],
				      cd.get('email','noreply@example.com'),
				      ['siteowner@example.com'],
				      connection=con
				      )
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
				initial = {'subject':'initial subject'}
			)

	return render(request,'contact_form.html',{'form':form})	

def contact_thanks(request):
	return HttpResponse('Thanks')