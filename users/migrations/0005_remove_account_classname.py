# Generated by Django 2.2.9 on 2020-06-19 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_account_classname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='classname',
        ),
    ]
