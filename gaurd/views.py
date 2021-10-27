from django.shortcuts import render,redirect
from .models import gaurds
from .models import guest_enteries
import datetime
# Create your views here.
def gaurd(request):
	if request.session.get('guser'):
		return redirect('ghome')
	else:
		return render(request,'gaurd.html')
	
def glogin(request):
	username = request.POST['guser']
	password = request.POST['gpass']
	
	res = gaurds.objects.filter(guser=username,gpass=password)
	
	if len(res)==1:
		request.session['guser']=res[0].guser
		return redirect('ghome')
	else:
		return render(request,'gaurd.html',{'error':'Username or Password Incorrect!!!'})

def ghome(request):
	if request.session.get('guser'):
		return render(request,'ghome.html')
	else:
		return redirect('/gaurd/')
		
def glogout(request):
	del request.session['guser']
	return redirect('/gaurd/')
	
def enter(request):
	if request.session.get('guser'):
		return render(request,'enter.html')
	else:
		return redirect('/gaurd/')
		
def insert_entry(request):
	guest_name = request.POST['guest_name']
	purpose = request.POST['purpose']
	comefrom = request.POST['comefrom']
	
	intime = datetime.datetime.now().replace(microsecond=0)
	
	q = guest_enteries(intime=intime, guest_name=guest_name, purpose=purpose, comefrom=comefrom)
	q.save()
	
	return render(request,'enter.html',{'info':'Entry inserted successfully.'})
	
def chk_entries(request):
	if request.session.get('guser'):
		res = guest_enteries.objects.all()
		return render(request,'chk_entries.html',{'res':res})
	else:
		return redirect('/gaurd/')

def exit(request):
	if request.session.get('guser'):
		res = guest_enteries.objects.all()
		return render(request,'exit.html',{'res':res})
	else:
		return redirect('/gaurd/')
		
def update_exit(request):
	extime = datetime.datetime.now().replace(microsecond=0)
	
	id = request.GET['id']
	
	k = guest_enteries.objects.get(id=id)
	k.extime=extime
	k.save()
	
	return render(request,'ghome.html',{'info':'Exit updated successfully.'})
	