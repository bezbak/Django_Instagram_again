from django.shortcuts import render
from .models import Chat
from django.db.models import Q
# Create your views here.
def chats(request):
    chats = Chat.objects.all().filter(Q(from_user = request.user) | Q(to_user=request.user))
    context = {
        'chats':chats
    }
    return render(request, 'chats.html', context)