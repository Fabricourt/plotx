# Generated by Django 2.2.9 on 2020-05-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200522_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subjects',
        ),
    ]
