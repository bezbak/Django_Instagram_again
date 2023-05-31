from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to="profile_images/"
    )
    description = models.CharField(
        max_length=555,
        blank=True,
        null=True
    )
    
class Follow(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='follows',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='followers',
        on_delete=models.CASCADE
    )