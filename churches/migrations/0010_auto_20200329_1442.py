# Generated by Django 2.2.9 on 2020-03-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0009_video_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
