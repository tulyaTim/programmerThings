from django.shortcuts import render, redirect
from .models import Post, UserProfile
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def community(request):
    userprofiles = UserProfile.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, 'community.html', 
                 {
                     'userprofiles':userprofiles,
                     'posts':posts,
                     'form':form,
                     'signup_form':signup_form,
                 }
    )

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')  # Replace with the name of your community view
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password')
    else:
        form = UserCreationForm()
    return render(request, 'master.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'master.html', {'form':form})

def login_required_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form':form})

@login_required
def details(request, id):
    userprofile = UserProfile.objects.get(id=id)
    return render(request, 'details.html', {'userprofile':userprofile})

@login_required
def Profile_edit(request, pk):
    userprofile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Incomplete')
    else:
        form = ProfileForm(instance=userprofile)
    return render(request, 'profile.html', {'form':form})
