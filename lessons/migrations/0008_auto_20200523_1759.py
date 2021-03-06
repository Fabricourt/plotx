# Generated by Django 2.2.9 on 2020-05-23 14:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20200523_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='ans_pic',
            field=models.ImageField(blank=True, null=True, upload_to='ans_pics/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='ans_video',
            field=models.FileField(blank=True, null=True, upload_to='ans_videos/'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='ans_video_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='answer',
            field=ckeditor.fields.RichTextField(help_text='create answers for the exercises you created here', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='ex_pic',
            field=models.ImageField(blank=True, help_text='if you need to use a picture for setting your question addit here or paste it in the exercise field abover', null=True, upload_to='ex_pics/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='ex_video',
            field=models.FileField(blank=True, null=True, upload_to='ex_videos/'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='ex_video_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_exercise',
            field=ckeditor.fields.RichTextField(help_text='create exercises for this lesson', null=True),
        ),
    ]
