from django.shortcuts import render, redirect
from .forms import CreatePostForm
from .models import CreatePost

# Create your views here.

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            return redirect('/')
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form':form})

def view_posts(request):
    posts = CreatePost.objects.all()
    return render(request, 'posts.html', {'posts':posts})
