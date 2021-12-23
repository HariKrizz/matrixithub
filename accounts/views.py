from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import redirect, render
from django.contrib import messages

def userRegister(request):
    if request.method =='POST':
        Username = request.POST["username"]
        Firstname = request.POST["firstname"]
        Lastname = request.POST["lastname"]
        mail = request.POST["email"]
        Passwd1 = request.POST["password1"]
        Passwd2 = request.POST["password2"]

        if Passwd1 == Passwd2:
            if User.objects.filter(username=Username).exists():
                messages.warning(request,"Username exists!")
                return redirect('register')

            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email already taken!")
                return redirect('register')
                
            else:
                obj = User.objects.create_user(username=Username,first_name=Firstname,last_name=Lastname,email=mail,password=Passwd1)
                obj.save()
                return redirect('login')
        else:
            messages.info(request,"Password does not match!")
            return redirect('register')
    else:
        return render(request,'Registration.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        passwd = request.POST['Password']
        user = auth.authenticate(username=username,password=passwd)

        if user is None:
            messages.warning(request,"Invalid Username or Password")
            return redirect('login') 
        else:
            auth.login(request,user)
            
            return redirect('/')
    else:
        return render(request, 'Login.html')
    
def userLogout(request):
    auth.logout(request)
    return redirect('/')