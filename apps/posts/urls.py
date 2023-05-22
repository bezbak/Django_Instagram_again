from django.urls import path
from apps.posts.views import index, create_post, post_detail

urlpatterns = [
    path("", index, name = "index"),
    path("create_post/", create_post, name = "create_post"),
    path("post_detail/<int:id>/", post_detail, name = "post_detail"),
]
