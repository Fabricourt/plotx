# Generated by Django 2.2.9 on 2020-04-20 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('towns', '0003_auto_20200417_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='town',
            name='town_pic1',
            field=models.ImageField(null=True, upload_to='towns/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='town',
            name='town_pic2',
            field=models.ImageField(null=True, upload_to='towns/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='town',
            name='town_pic',
            field=models.ImageField(null=True, upload_to='towns/%Y/%m/%d/'),
        ),
    ]
