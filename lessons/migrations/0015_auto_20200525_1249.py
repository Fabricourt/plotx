# Generated by Django 2.2.9 on 2020-05-25 09:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_auto_20200525_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_question',
            name='Explanation',
        ),
        migrations.AlterField(
            model_name='exercise_question',
            name='corrans',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
