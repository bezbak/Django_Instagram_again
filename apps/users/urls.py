from django.urls import path
from apps.users.views import register, user_login,profile, profile_update
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("profile/<str:username>/", profile, name = "profile"),
    path("profile_update/<str:username>/", profile_update, name = "profile_update"),
    path("register/", register, name = "register"),
    path("login/", user_login, name = "login"),
    path("logout/", LogoutView.as_view(next_page="login"), name = "logout"),
]
