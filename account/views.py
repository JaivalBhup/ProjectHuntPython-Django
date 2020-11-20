from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['cpass']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request, 'account/signup.html', {"error": "The User already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['uname'], password=request.POST['pass'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {"error": "The passwords does not match"})
    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method=="POST":
        user = auth.authenticate(username=request.POST['uname'], password=request.POST['pass'])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {"error": "Incorrect Username or password"})
    return render(request, 'account/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')

