# Generated by Django 2.2.9 on 2020-06-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20200626_1601'),
        ('lessons', '0022_auto_20200626_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video',
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.ManyToManyField(help_text='select videos for this lessons', to='videos.Video'),
        ),
    ]
