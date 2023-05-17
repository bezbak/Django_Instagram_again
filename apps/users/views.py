from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import User
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        profile_image = request.FILES.get("profile_image")
        if password == confirm_password:
            user = User.objects.create(username=username, profile_image=profile_image)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username, password = password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    return render(request, 'register.html')