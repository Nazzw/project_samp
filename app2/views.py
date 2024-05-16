from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        usname=request.POST['username']
        psw=request.POST['psw']
        repsw=request.POST['psw-repeat']
        if psw!=repsw:
            messages.info(request,'passwords are not matching')
            return redirect('signup')
        elif User.objects.filter(username=usname).exists():
            messages.info(request,'username already exists')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already exists')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=usname,first_name=fname,last_name=lname,email=email,password=psw)
            user.save()
            print('user ragistered')
            return redirect('/')
        
        
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        usname=request.POST['usname']
        psw=request.POST['psw']
        user=auth.authenticate(username=usname,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info (request,'invalid candidate')
            return redirect("login")
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

