from django.shortcuts import render, redirect
from apps.posts.models import Posts
# Create your views here.

def index(request):
    posts = Posts.objects.all()
    context = {
        "posts":posts
    }
    return render(request, "index.html",context)

def create_post(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        descr = request.POST.get("descr")
        if request.user.is_authenticated:
            post = Posts.objects.create(image = image, description = descr, post_user = request.user)
            post.save()
            return redirect("index")
    return render(request, "create_post.html")