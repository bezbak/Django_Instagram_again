from django.urls import path
from apps.posts.views import index

urlpatterns = [
    path("", index, name = "index"),
]
