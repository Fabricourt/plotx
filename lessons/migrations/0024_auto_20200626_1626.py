# Generated by Django 2.2.9 on 2020-06-26 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20200626_1601'),
        ('lessons', '0023_auto_20200626_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video',
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='videos.Video'),
        ),
    ]
