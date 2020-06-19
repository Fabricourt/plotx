# Generated by Django 2.2.9 on 2020-05-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='slug',
            field=models.SlugField(help_text='You must re enter the class name using dashes e.g class 7 west = class-7-west on the slug field', max_length=250, null=True, unique_for_date='date_posted'),
        ),
    ]
