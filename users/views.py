from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import auth
from .models import User
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form_password = form.clean_password2()
            form = form.save(commit=False)
            form.save()
            username = form.username
            password = form.password
            print(username, password)

            auth_login = auth.authenticate(username=username, password=form_password)
            auth.login(request, auth_login)
            return redirect("home")
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

