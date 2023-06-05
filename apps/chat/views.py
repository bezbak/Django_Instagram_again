from django.shortcuts import render, redirect
from .models import Chat, Message
from django.db.models import Q
# Create your views here.
def chats(request):
    chats = Chat.objects.all().filter(Q(from_user = request.user) | Q(to_user=request.user))
    context = {
        'chats':chats
    }
    return render(request, 'chats.html', context)

def chat_detail(request, id):
    chat = Chat.objects.get(id=id)
    if request.method == 'POST':
        text =request.POST.get('text')
        message = Message.objects.create(text = text, from_user= request.user, chat = chat)
        return redirect('chat_detail', chat.id)
    context = {
        'chat':chat
    }
    return render(request, 'chat_detail.html', context)