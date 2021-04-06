# Generated by Django 2.2.9 on 2020-07-06 05:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_student_is_mvp'),
        ('subjects', '0010_subject_teacher'),
        ('teachers', '0005_teacher_is_mvp'),
        ('exam_room', '0002_exampaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='status',
            field=models.IntegerField(choices=[(0, 'Wrong'), (1, 'Correct')], default=0),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='marked',
            field=models.IntegerField(choices=[(0, 'Unmarked'), (1, 'Marked')], default=0),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
    ]