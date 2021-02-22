from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
            
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/login")

def index(request):
    return render (request,'index.html')

def about(request):
    return render(request,'about.html')

def signuser(request):
    form = UserCreationForm()
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    context={'form':form}
    return render(request,'signup.html',context)

def services(request):
    #return HttpResponse("This is Servicespage")
    return render(request,'services.html')

def contacts(request):
    #return HttpResponse("This is Contactpage")
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name, email=email,phone=phone,date=datetime.today())
        contact.save()
    return render(request,'contacts.html')