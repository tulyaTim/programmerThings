from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    template = loader.get_template('new.html')
    context = {
        'form':form,
    }
    return HttpResponse(template.render(context, request))   

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    template = loader.get_template('inbox.html')
    context = {
         'conversations':conversations,
    }
    return HttpResponse(template.render(context, request))

def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'post':
        form = ConversationMessageForm(request.POST)

        if form.is_valid:
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('converstion:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    template = loader.get_template('detail.html')
    context = {
        'conversation':conversation,
        'form':form,
    }

    return HttpResponse(template.render(context, request))
    