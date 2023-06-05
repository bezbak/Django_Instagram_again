from django.db import models
from apps.users.models import User
# Create your models here.
class Chat(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='from_chats',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='to_chats',
        on_delete=models.CASCADE
    )
    
class Message(models.Model):
    text = models.CharField(
        max_length=555
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    chat = models.ForeignKey(
        Chat,
        related_name="messages",
        on_delete=models.CASCADE
    )
    from_user = models.ForeignKey(
        User,
        related_name='from_message',
        on_delete=models.CASCADE
    )