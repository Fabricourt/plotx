# Generated by Django 2.2.9 on 2020-07-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200701_0513'),
        ('classes', '0018_auto_20200622_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_name',
            name='account',
            field=models.ManyToManyField(blank=True, help_text='pick authorized personel to view class', to='users.Account'),
        ),
    ]
