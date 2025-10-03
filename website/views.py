from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        
    return render(request, 'home.html', {})


def logout_user(request):
    pass
