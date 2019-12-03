from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index (request):
    return render(request,'index.html')

def login (request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password1']
            pasword2 = form.cleaned_data.get['pasword2']
            user = authenticate(username = username, password = password)
            login(request, user)
            return render(request, 'index.html')

    else:
        form = UserCreationForm()

    return render(request,'registration/register.html', {'form' : form})
