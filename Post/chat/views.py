from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageForm
from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


@login_required
def chat_view(request, user_id):
    user = request.user
    recipient = get_object_or_404(User, id=user_id)

    # Get the conversation between the logged-in user and the recipient
    messages = Message.objects.filter(
        (models.Q(sender=user.id) & models.Q(receiver=recipient.id)) |
        (models.Q(sender=recipient.id) & models.Q(receiver=user.id))
    ).order_by('timestamp')

    # Handle form submission for new messages
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = user
            new_message.receiver = recipient
            new_message.save()
            return redirect('chat:chat_view', user_id=user_id)  # Redirect to refresh the page
    else:
        form = MessageForm()

    context = {
        'recipient': recipient,
        'messages': messages,
        'form': form,
    }
    return render(request, 'chat.html', context)


