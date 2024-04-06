from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Password not match")

        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or Password is incorrect !!!")

    return render(request, 'login.html')


# @login_required(login_url='login')
def HomePage(request):
    return render(request, 'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

def aboutus(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

# def aboutus2(request):
#     return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



