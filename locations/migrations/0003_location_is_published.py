# Generated by Django 2.2.9 on 2020-01-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20200117_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]