# Generated by Django 2.2.9 on 2020-05-25 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
    ]
