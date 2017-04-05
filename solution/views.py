from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Details, Pending
import datetime
import requests


# Create your views here.
#from .models import
from django.contrib.auth import authenticate, login, logout
from twilio.rest import TwilioRestClient


def login_site(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = username, password = password)

		if user:
			login(request, user)
			return redirect('/index/')
		else:
			return HttpResponse('invalid')	


	else:	
		return render(request, 'login.html')

	return render(request, 'login.html')
	
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa0fc6147607d4eb6a3e315a2b9ac6c99.mailgun.org/messages",
        auth=("api", "YOUR MAILGUN API KEY"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxa0fc6147607d4eb6a3e315a2b9ac6c99.mailgun.org>",
              "to": "Name <Email id>",
              "subject": "Subject of mail",
              "text": "Body of the mail"})

def hello():
	ACCOUNT_SID = 'YOUR TWILIO ACCOUNT SID'
	AUTH_TOKEN = 'YOUR TWILIO AUTH TOKEN'
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	client.messages.create(to = 'NUMBER YOU WANT TO SEND MESSAGE',from_ = 'YOUR TWILIO NUMBER', body = 'BODY OF MESSAGE',)
	return 0





def index(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			sap_id = request.POST['sapid']
			p = Pending.objects.all()
			for i in p:
				if i.sapid.sap == sap_id:
					return render(request,'index.html',{'message':"You cannot Do that"})
				else:	
					name = request.POST['name']
					dep = request.POST['dep']
					year = request.POST['year']
					division = request.POST['division']
					email = request.POST['email']
					phone = request.POST['phone']
					address=request.POST['address']
					source = request.POST['ss']
					destination = request.POST['ds']
					railway_class = request.POST['class']
					dob = request.POST['dob']
					gender = request.POST['gender']
					details = Details.objects.create(sap = sap_id, name = name, email = email, phone = phone, address = address,
				                             source = source, destination = destination, bday = dob, year = year,
				                             department = dep, division = division, status = "Submitted", is_submitted = True,
				                             rail_class = railway_class, gender = gender, time = datetime.date.today() )


					a = Details.objects.get(sap = sap_id)
			#print a.sap

					pend = Pending()
					pend.sapid = a
					pend.save()

					send_simple_message()
					hello()



					return redirect('/detail/')
		else:
			return render(request, "index.html")
	else:
		return render(request,"login.html")


def detail(request):
	if request.user.is_authenticated():
		p = request.user.username
		#return HttpResponse(p)
		
		b = Details.objects.get(pk=p)
		context = {'b':b}
		return render(request,"detail.html",context)
	else:
		return render(request, 'login.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect('/adminpage/')
        else:	
            return HttpResponse('invalid Credentialllllls')    


    else:    
        return render(request, 'adminlogin.html')

    return render(request, 'adminlogin.html')


def adminpage(request):
    if request.user.is_superuser:
        p = Pending.objects.all()
        context = {'p':p}
        return render(request,'admindetail .html',context)
    else:
    	return HttpResponse("Invalid Credentialssss")


def update(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			s = request.POST['ready']
			c = Pending.objects.get(pk = s)
			c.sapid.status = "Ready"
			c.sapid.save()
			c.delete()
			return redirect('/adminpage/')
		else:
			return redirect('/adminpage/')	
	else:
		return render(request, 'adminlogin.html')	



def logout_site(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('/login/')
	else:
		return HttpResponse('You need to log in')










