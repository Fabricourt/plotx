# Generated by Django 2.2.9 on 2020-06-22 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0017_auto_20200621_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Grade', 'verbose_name_plural': 'Grades'},
        ),
        migrations.DeleteModel(
            name='Classx',
        ),
    ]