# Generated by Django 2.2.9 on 2020-05-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0016_auto_20200527_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(null=True),
        ),
    ]