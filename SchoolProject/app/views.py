from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['usr1']
        password = request.POST['ps1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('red')

        else:
            messages.info(request, "invalid credential")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        psswrd = request.POST['password']
        cpsswrd = request.POST['confirm-password']
        if psswrd == cpsswrd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=psswrd)
                user.save()


        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('login')

    return render(request, 'register.html')


def form(request):
    return render(request, 'form.html')


def red(request):
    return render(request, 'redirect.html')


def order(request):
    return render(request, 'order.html')


def logout(request):
    auth.logout(request)
    return redirect('login')