# Generated by Django 2.2.9 on 2020-06-19 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0014_auto_20200609_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-created_on']},
        ),
    ]
