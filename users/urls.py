from django.urls import path
from .views import register
from users.middlewares.auth import LogoutCheckMiddleware
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("register/", LogoutCheckMiddleware(register), name="register"),
    path("login/", LogoutCheckMiddleware(auth_view.LoginView.as_view(template_name="users/login.html")), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout")

]