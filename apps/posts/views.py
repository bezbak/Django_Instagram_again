from django.shortcuts import render
from apps.posts.models import Posts
# Create your views here.

def index(request):
    posts = Posts.objects.all()
    context = {
        "posts":posts
    }
    return render(request, "index.html",context)