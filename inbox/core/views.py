from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

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
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(participants=request.user)
    return render(request, 'chat/inbox.html', {'conversations':conversations})

@login_required
def conversation_detail(request, pk):
        conversation = Conversation.objects.get(pk=pk)
        if request.user not in conversation.participants.all():
            return redirect('inbox')
        messages = conversation.messages.all()
        for message in messages:
            if message.sender != request.user:
                message.read = True
                message.save()
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                new_message = form.save(commit=False)
                new_message.sender = request.user
                new_message.conversation = conversation
                new_message.save()
                return redirect('conversation_detail', pk=conversation.pk)
            else:
                form = MessageForm()
            return render(request, 'chat/conversation.html', {'form':form})
