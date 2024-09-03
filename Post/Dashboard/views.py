from django.shortcuts import render, redirect
from .models import Post, UserProfile
from django.contrib.auth.decorators import login_required
from .forms import PostForm

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

def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'posts': posts})
