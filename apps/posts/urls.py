from django.urls import path
from apps.posts.views import index, create_post, post_detail, post_update, post_del

urlpatterns = [
    path("", index, name = "index"),
    path("create_post/", create_post, name = "create_post"),
    path("post_detail/<int:id>/", post_detail, name = "post_detail"),
    path("post_update/<int:id>/", post_update, name = "post_update"),
    path("post_del/<int:id>/", post_del, name = "post_del"),
]
