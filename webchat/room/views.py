from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def rooms(request, slug):
    rooms = Room.objects.get(slug=slug)

    return render(request, 'room/rooms.html', {'room': Room})