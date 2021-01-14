from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'chatapp/index.html')

def room(req, room_name):
    return render(req, 'chatapp/room.html', {
        'room_name': room_name
    })