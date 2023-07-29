from django.contrib.auth.models import User
from django.db import models
# from djmoney.models.fields import MoneyField


class ExpensesCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    datetime = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ("title",)
        verbose_name = "Категория расходов"

    def __str__(self):
        return f"{self.title} {self.datetime}"


class IncomesAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "Счет доходов"

    def __str__(self):
        return f"{self.title} {self.datetime}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"

    def __str__(self):
        return f"{self.sum} {self.category} {self.datetime}"


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(IncomesAccount, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"

    def __str__(self):
        return f"{self.sum} {self.account} {self.datetime}"
