import accounts
from django.shortcuts import render , redirect
from notesapp.models import text
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        if User.objects.filter(username=username).exists():
            data={}
            data['error']="User already exist"
            return render(request,'notesapp/signup.html',data)
        else:
            user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
            return redirect("/accounts/login/")
    else:
        return render(request,'notesapp/signup.html')

def login(request):
    if request.method == "POST":
        ema = request.POST['email']
        pword = request.POST['password']
        user = auth.authenticate(username=ema, password=pword)
        if user is not None:
            auth.login(request, user)
            request.session['email']=ema
            return redirect('/notes/newnote/')
        else:
            data = {}
            data['error'] = "Email or Password is incorrect"
            return render(request,'notesapp/login.html',data)
    else:
        return render(request, 'notesapp/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'notesapp/login.html')
