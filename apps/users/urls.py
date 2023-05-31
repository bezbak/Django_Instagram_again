from django.urls import path
from apps.users.views import register, user_login,profile
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("<str:username>/", profile, name = "profile"),
    path("register/", register, name = "register"),
    path("login/", user_login, name = "login"),
    path("logout/", LogoutView.as_view(next_page="login"), name = "logout"),
]
