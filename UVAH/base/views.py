from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def login(request):
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')

def webdev(request):
    return render(request, 'base/webdev.html')

def frontend(request):
    return render(request, 'base/frontend.html')

def backend(request):
    return render(request, 'base/backend.html')

