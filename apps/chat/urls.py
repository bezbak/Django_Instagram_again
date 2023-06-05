from django.urls import path
from apps.chat.views import chats, chat_detail
urlpatterns = [
    path('', chats, name='chats'),
    path('<int:id>/', chat_detail, name='chat_detail')
]
