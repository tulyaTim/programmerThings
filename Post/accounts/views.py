from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import UserProfile
from .forms import ProfileForm, CustomUserCreationForm
from Dashboard.models import Post

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request, id):
    userprofile = UserProfile.objects.get(pk=id)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'profile.html', {'userprofile': userprofile, 'posts':posts})

def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/')
    else:
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'profile_form': profile_form})