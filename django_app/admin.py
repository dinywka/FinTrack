from django.contrib import admin
from django_app import models

# Register your models here.
admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


admin.site.register(models.ExpensesCategory)
admin.site.register(models.IncomesAccount)
admin.site.register(models.Expense)
admin.site.register(models.Income)