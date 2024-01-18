from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import PasswordVault
from .forms import PasswordVaultForm, CustomUserCreationForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

#create view
def PasswordCreate(request):
    context = {}
    form =  PasswordVaultForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("Password create form is valid. Saved...")
    else:
        print("Form is not valid. Errors:", form.errors)
    context ['form'] = form
    return render(request, 'password_create.html', context)

def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page you want after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})