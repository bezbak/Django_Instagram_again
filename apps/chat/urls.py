from django.urls import path
from apps.chat.views import chats
urlpatterns = [
    path('', chats, name='chats')
]
