# Generated by Django 2.2.9 on 2020-05-23 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20200522_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='computer_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='english_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='home_science_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='kiswahili_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='maths_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='music_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='p_e_teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='social_studies_teacher',
        ),
    ]
