from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def home(request):
    return render(request, 'django_app/home.html')

def register(request):
    if request.method == "GET":
        return render(request, "django_app/register.html")
    elif request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        if (
                re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email) is None
        ):
            return render(
                request,
                "django_app/register.html",
                {"error": "Некорректный формат email или пароль"},
            )
        try:
            User.objects.create(
                username=email,
                password=make_password(password),
                email=email,
            )
        except Exception as error:
            return render(
                request,
                "django_app/register.html",
                {"error": str(error)},
            )
        return render(request, "django_app/list.html")
    else:
        raise ValueError("Invalid method")


def login_f(request):
    if request.method == "GET":
        return render(request, "django_app/login.html", {})
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email,
                            password=password)

        if user is None:
            raise Exception("ДАННЫЕ ДЛЯ ВХОДА НЕПРАВИЛЬНЫЕ!")
        else:
            login(request, user)
            return render(request, "django_app/list.html")
    else:
        raise Exception("Method not allowed!")


def logout_f(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""
    logout(request)
    return redirect(reverse('login'))


