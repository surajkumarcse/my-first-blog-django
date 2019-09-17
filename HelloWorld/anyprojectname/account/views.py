from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user == None:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')

        else:
            auth.login(request, user)
            messages.info(request, 'Password matched!')
            return redirect('/')
    
    else :
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['second_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email = email).exists():
            messages.info(request, 'message already taken!')
            return redirect('register')

        elif User.objects.filter(username = username).exists():
            messages.info(request, 'username already taken!')
            return redirect('register')

        elif password1 != password2:
            messages.info(request, 'password already taken!')
            return redirect('register')

        else:
            messages.info(request, 'username and password already taken')

            user = User.objects.create_user(username = username, password = password1, first_name = first_name, last_name = last_name, email = email)
            user.save()

            print('user successfully created!')
            return redirect('login')
            
    else:    
        return render(request, 'register.html')
