from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import logout , login 
from home.models import Signup

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        signup = Signup(username=username, email=email, address=address)
        signup.save();
    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect("/index")