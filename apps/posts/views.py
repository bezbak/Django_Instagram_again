from django.shortcuts import render, redirect
from apps.posts.models import Posts, Like, Comment
# Create your views here.

def index(request):
    posts = Posts.objects.all().order_by('-created')
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        if request.user.is_authenticated:
            try:
                like = Like.objects.get(user = request.user, post_id = post_id)
                like.delete()
                return redirect('index')
            except:
                like = Like.objects.create(user = request.user, post_id = post_id)
                like.save()
                return redirect('index')
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

def post_detail(request, id):
    post = Posts.objects.get(id = id)
    if request.method == 'POST' and request.user.is_authenticated:
        if 'like' in request.POST:
            try:
                like = Like.objects.get(user = request.user, post = post)
                like.delete()
                return redirect('post_detail', post.id)
            except:
                like = Like.objects.create(user = request.user, post = post)
                like.save()
                return redirect('post_detail', post.id)
        if 'comment' in request.POST:
            text = request.POST.get('text')
            comment = Comment.objects.create(text =text, post = post, user = request.user)
            comment.save()
            return redirect('post_detail', post.id)
    context = {
        "post":post
    }
    return render(request, "comment.html", context)

def post_update(request, id):
    post = Posts.objects.get(id = id)
    if request.method == 'POST':
        description = request.POST.get("descr")
        image = request.FILES.get('image')
        if image:
            post.description = description
            post.image = image
            post.save()
        else:
            post.description = description
            post.save()
        return redirect('post_detail', post.id)
    context = {
        "post":post
    }
    return render(request, "update_post.html", context)

def post_del(request, id):
    post = Posts.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect('index')
    context = {
        'post':post
    }
    return render(request, 'delete_post.html', context)