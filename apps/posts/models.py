from django.db import models
from apps.users.models import User
# Create your models here.
class Posts(models.Model):
    image = models.ImageField(
        upload_to="post_images/"
    )
    description = models.TextField(
        max_length=500
    )
    post_user = models.ForeignKey(
        User,
        related_name="post_user",
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

class Like(models.Model):
    post = models.ForeignKey(
        Posts,
        related_name='likes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="likes",
        on_delete=models.CASCADE
    )