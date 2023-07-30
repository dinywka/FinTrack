from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



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
    amount = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE)

    def get_model_type(self):
        return "expense"

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"

    def __str__(self):
        return f"{self.amount} {self.category} {self.datetime}"


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(IncomesAccount, on_delete=models.CASCADE)

    def get_model_type(self):
        return "income"

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"

    def __str__(self):
        return f"{self.amount} {self.account} {self.datetime}"


@receiver(post_save, sender=User)
def create_default_category(sender, instance, created, **kwargs):
    if created:
        ExpensesCategory.objects.create(user=instance, title='Продукты')
        IncomesAccount.objects.create(user=instance, title='Общий')
