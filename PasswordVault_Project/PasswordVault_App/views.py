from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import PasswordVault
from .forms import PasswordVaultForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

#create view
@login_required
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

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['password2']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

def Logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
    return render(request, 'logout.html')