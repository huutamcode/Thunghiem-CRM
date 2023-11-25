from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    # Check to see if logging in
    if request.method=="POST":
        username = request.POST['username']
    return render(request, 'home.html', {} )

def login_user(request):
    pass

def logout_user(request):
    pass

