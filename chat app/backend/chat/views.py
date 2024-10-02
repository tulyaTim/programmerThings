from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q 

@login_required
def private_messages(request, user_id):
    receiver = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=receiver)) | 
        (Q(sender=receiver) & Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST['message']
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('private_messages', user_id=user_id)

    return render(request, 'private_messages.html', {
        'receiver': receiver,
        'messages': messages
    })
