# Generated by Django 2.2.9 on 2020-06-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20200603_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.AddField(
            model_name='answer',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]