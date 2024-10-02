from django.shortcuts import render, redirect
from .models import Members
from .forms import Members_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_members(request):
    members = Members.objects.all()
    return render(request, 'members.html', {'members':members})

@login_required
def add_members(request):
    if request.method == 'POST':
        form = Members_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members')
    else:
        form = Members_form()
    return render(request, 'add_members.html', {'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')