# Generated by Django 2.2.9 on 2020-05-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice_board', '0002_auto_20200524_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='slug',
            field=models.SlugField(help_text='repeat the title here replace spaces with dashes e.g. class alert = class-alert', max_length=250, null=True, unique_for_date='date_posted'),
        ),
    ]
