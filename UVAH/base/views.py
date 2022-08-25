from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Subtopic, Course
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return redirect('roadmap')

def roadmap(request):
    return render(request, 'base/home.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect("roadmap")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("roadmap")
        else:
            messages.info(request, "Try again! Email or Password is incorrect")
        

    return render(request, 'base/login.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect("roadmap")

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("roadmap")
    
    form = UserForm()
    context = {"form": form}

    return render(request, 'base/register.html', context)

def user_logout(request):
    logout(request)
    return redirect("roadmap")

def webdev(request):
    return render(request, 'base/webdev.html')

def frontend(request):
    return render(request, 'base/frontend.html')

def backend(request):
    return render(request, 'base/backend.html')

def profile(request):

    return render(request, 'base/profile.html')

def submitCourse(request):
    return render(request, 'base/submitCourse.html')

def test(request):
    data = User.objects.all()
    
    context = {"users": data}

    return render(request, "base/test.html", context)
