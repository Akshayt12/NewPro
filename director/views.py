from django.shortcuts import render,redirect
from .models import director_login
from gaurd.models import gaurds
from gaurd.models import guest_enteries
# Create your views here.
def director(request):
	if request.session.get('user'):
		return redirect('home')
	else:
		return render(request,'director.html')
	
def dlogin(request):
	username = request.POST['duser']
	password = request.POST['dpass']
	
	res = director_login.objects.filter(duser=username,dpass=password)
	
	if len(res)==1:
		request.session['user']=res[0].duser
		return redirect('home')
	else:
		return render(request,'director.html',{'error':'Username or Password Incorrect!!!'})

def home(request):
	if request.session.get('user'):
		return render(request,'home.html')
	else:
		return redirect('/director/')

def logout(request):
	del request.session['user']
	return redirect('/director/')
	
def account(request):
	if request.session.get('user'):
		return render(request,'account.html')
	else:
		return redirect('/director/')

def create_account(request):
	username = request.POST['guser']
	first_name = request.POST['gfname']
	last_name = request.POST['glname']
	password = request.POST['gpass']

	res = gaurds.objects.filter(guser=username)
	if len(res)>0:
		return render(request,'account.html',{'error':'Gaurd is already exists with given username.'})
	else:
		q = gaurds(guser=username, gfname=first_name, glname=last_name, gpass=password)
		q.save()
		return render(request,'account.html',{'error':'Account has been created successfully.'})

def check(request):
	res = guest_enteries.objects.all()
	
	return render(request,'check.html',{'res':res})