from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect('roadmap')

def roadmap(request):
    return render(request, 'base/home.html')

def user_login(request):
    

    return render(request, 'base/login.html')

def user_register(request):
    print("hello world")
    if request.user.is_anonymous:
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
    else:
        return redirect('roadmap')
    
    form = UserForm()
    context = {"form": form}

    return render(request, 'base/register.html', context)

def webdev(request):
    return render(request, 'base/webdev.html')

def frontend(request):
    return render(request, 'base/frontend.html')

def backend(request):
    return render(request, 'base/backend.html')

def submit(request):
    return render(request, 'base/submit.html')

def test(request):
    data = User.objects.all()
    context = {"users": data}

    return render(request, "base/test.html", context)
