from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.

def home_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        try:
            existing_room = Room.objects.get(room_name__icontains=room)
        except:
            r = Room.objects.create(room_name=room)
        return redirect('room', username=username, room_name=room)
    return render(request, 'home.html')

def room_view(request, room_name, username):
    existing_room = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room=existing_room)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": existing_room.room_name,
    }
    return render(request, 'room.html', context)