# Generated by Django 2.2.9 on 2020-05-22 08:34

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0003_subject_class_level'),
        ('teachers', '0002_auto_20200522_1049'),
        ('classes', '0005_auto_20200522_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=100, null=True)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('lesson_pic', models.ImageField(blank=True, null=True, upload_to='lesson_pics/%Y/%m/%d/')),
                ('lesson_video_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('lesson_video', models.FileField(blank=True, null=True, upload_to='lesson_videos/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_mvp', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Topic')),
            ],
        ),
    ]
