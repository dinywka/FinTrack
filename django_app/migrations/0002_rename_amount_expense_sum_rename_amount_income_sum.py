# Generated by Django 4.2.3 on 2023-07-28 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='amount',
            new_name='sum',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='amount',
            new_name='sum',
        ),
    ]
