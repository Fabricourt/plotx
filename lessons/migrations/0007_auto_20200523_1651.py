# Generated by Django 2.2.9 on 2020-05-23 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_auto_20200523_1117'),
        ('lessons', '0006_auto_20200523_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_answer',
            options={'ordering': ('date_posted',)},
        ),
        migrations.AlterModelOptions(
            name='teacher_answer',
            options={'ordering': ('date_posted',)},
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='question',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='student_answer',
            old_name='created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='student_answer',
            old_name='active',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='teacher_answer',
            old_name='created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='teacher_answer',
            old_name='active',
            new_name='is_published',
        ),
        migrations.RemoveField(
            model_name='student_answer',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='teacher_answer',
            name='updated',
        ),
        migrations.AddField(
            model_name='exercise',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='date_posted'),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='ex_lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lessons.Lesson'),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='ex_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='ex_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lessons.Topic'),
        ),
        migrations.AddField(
            model_name='student_answer',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='date_posted'),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='diagram',
            field=models.ImageField(blank=True, null=True, upload_to='diagrams/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='ex_ans_video',
            field=models.FileField(blank=True, null=True, upload_to='lesson_videos/'),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='ex_ans_video_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='ex_lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lessons.Lesson'),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='ex_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='ex_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lessons.Topic'),
        ),
        migrations.AddField(
            model_name='teacher_answer',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='date_posted'),
        ),
    ]
