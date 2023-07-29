from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExpensesCategory, IncomesAccount, Expense, Income
from itertools import chain


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
                HttpResponse("Возникла ошибка! Попробуйте снова"),
                {"error": str(error)},
            )
        return render(request, "django_app/login.html")
    else:
        raise ValueError("Invalid method")


def login_f(request):
    if request.method == "GET":
        return render(request, "django_app/login.html", {})
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is None:
            return render(request, "django_app/main.html", {"error": "ДАННЫЕ ДЛЯ ВХОДА НЕПРАВИЛЬНЫЕ!"})
        else:
            login(request, user)
            return redirect('main')
    else:
        return HttpResponseNotAllowed(["GET", "POST"])



def logout_f(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""
    logout(request)
    return redirect(reverse('login'))

#
# def main(request):
#     incomes_accounts = None
#     expenses_categories = None
#     incomes = None
#     expenses = None
#     if request.user.is_authenticated:
#         incomes_accounts = IncomesAccount.objects.filter(user=request.user)
#         expenses_categories = ExpensesCategory.objects.filter(user=request.user)
#         incomes = Income.objects.filter(user=request.user)
#         expenses = Expense.objects.filter(user=request.user)
#
#         if request.method == 'POST':
#             # Check if it's an income or an expense
#             if 'account' in request.POST:  # This is an income
#                 # Get the submitted data
#                 sum = request.POST.get('sum')
#                 account_id = request.POST.get('account')
#                 print(f"Sum: {request.POST.get('sum')}")
#
#                 # Fetch the account from the database
#                 account = IncomesAccount.objects.get(id=account_id)
#
#                 # Create a new Income object and save it to the database
#                 income = Income(user=request.user, sum=sum, account=account)
#                 income.save()
#
#             elif 'category' in request.POST:  # This is an expense
#                 # Get the submitted data
#                 sum = request.POST.get('sum')
#                 category_id = request.POST.get('category')
#
#                 # Fetch the category from the database
#                 category = ExpensesCategory.objects.get(id=category_id)
#
#                 # Create a new Expense object and save it to the database
#                 expense = Expense(user=request.user, sum=sum, category=category)
#                 expense.save()
#
#             #todo
#             elif 'new_account' in request.POST:
#                 title = request.POST.get('title', None)
#                 IncomesAccount.objects.create(user=request.user, title=title)
#                 return redirect('main')
#
#             elif 'new_expense_category' in request.POST:
#                 title = request.POST.get('title', None)
#                 ExpensesCategory.objects.create(user=request.user, title=title)
#                 return redirect('main')
#
#             # Redirect to the same page after form submission
#             return render(request, 'django_app/main.html', {
#                 'incomes_accounts': incomes_accounts,
#                 'expenses_categories': expenses_categories,
#                 'incomes': incomes,
#                 'expenses': expenses,
#             })
#
#     else:
#         incomes_accounts = None
#         expenses_categories = None
#
#     return render(request, 'django_app/main.html', {
#         'incomes_accounts': incomes_accounts,
#         'expenses_categories': expenses_categories,
#         'incomes': incomes,
#         'expenses': expenses,
#     })


def main(request):
    if request.method == 'POST':
        if 'account' in request.POST:  # This is an income
                        # Get the submitted data
            sum = request.POST.get('sum')
            account_id = request.POST.get('account')
            print(f"Sum: {request.POST.get('sum')}")

                        # Fetch the account from the database
            account = IncomesAccount.objects.get(id=account_id)

                        # Create a new Income object and save it to the database
            income = Income(user=request.user, sum=sum, account=account)
            income.save()

        elif 'category' in request.POST:  # This is an expense
                        # Get the submitted data
            sum = request.POST.get('sum')
            category_id = request.POST.get('category')

                        # Fetch the category from the database
            category = ExpensesCategory.objects.get(id=category_id)

                        # Create a new Expense object and save it to the database
            expense = Expense(user=request.user, sum=sum, category=category)
            expense.save()

                    #todo
        elif 'new_account' in request.POST:
            title = request.POST.get('title', None)
            IncomesAccount.objects.create(user=request.user, title=title)
            return redirect('main')

        elif 'new_expense_category' in request.POST:
            title = request.POST.get('title', None)
            ExpensesCategory.objects.create(user=request.user, title=title)
            return redirect('main')
        return redirect('main')

    incomes_accounts = None
    expenses_categories = None
    incomes = None
    expenses = None
    if request.user.is_authenticated:
        incomes_accounts = IncomesAccount.objects.filter(user=request.user)
        expenses_categories = ExpensesCategory.objects.filter(user=request.user)
        incomes = Income.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        table_incomes = [(income, 'income') for income in Income.objects.filter(user=request.user)]
        table_expenses = [(expense, 'expense') for expense in Expense.objects.filter(user=request.user)]

        transactions = list(chain(table_expenses, table_incomes))
        transactions.sort(key=lambda x: x[0].datetime, reverse=True)

    return render(request, 'django_app/main.html', {
        'transactions': transactions,
        'incomes_accounts': incomes_accounts,
        'expenses_categories': expenses_categories,
        'incomes': incomes,
        'expenses': expenses,
    })




