from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']  # Added 'POST' to retrieve the value

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')  # Updated the URL to use the name of the view function
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register')  # Updated the URL to use the name of the view function
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                return redirect('/')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register') 
    return render(request, 'register.html') # Updated the URL to use the name of the view function

        

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        # Perform login logic here
        # ...
        return redirect('index')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
  

    