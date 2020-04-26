# Generated by Django 2.2.9 on 2020-04-22 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('churches', '0003_auto_20200422_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='church',
            name='members',
        ),
        migrations.AddField(
            model_name='church',
            name='churchmember',
            field=models.ManyToManyField(blank=True, help_text='Select this church members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='church',
            name='created_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
