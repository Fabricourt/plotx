# Generated by Django 2.2.9 on 2020-07-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200618_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]
