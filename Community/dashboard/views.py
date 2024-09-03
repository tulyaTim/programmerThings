from django.shortcuts import render, redirect
from .models import Post, UserProfile
from django.http import JsonResponse
from .forms import UserProfileForm, AddPostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

def community_view(request):
    userprofiles = UserProfile.objects.all()
    posts = Post.objects.all()
    return render(request, 'community.html', {'posts': posts, 'userprofiles':userprofiles})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {'form':form})

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save(commit=False)
            name.name = request.user
            name.save()
            return redirect('/')
    else:
        form = UserProfileForm()
    return render(request, 'create_profile.html', {'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def like_post(request):
    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post_id = form[post_id]
            post = Post.objects.get(id=post_id)
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            if like:
                like.delete()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        ...

def profile_details(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm()
    return render(request, 'profile.html', {'form':form})
