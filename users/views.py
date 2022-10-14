from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import auth
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form_password = form.clean_password2()
            form = form.save(commit=False)
            email = form.email
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect("register")
            else:
                form.save()
                auth_login = auth.authenticate(username=form.username, password=form_password)
                auth.login(request, auth_login)
                return redirect("home")
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, 'error')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, '', context)

