# Generated by Django 2.2.9 on 2020-05-25 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_classname'),
        ('lessons', '0009_auto_20200523_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='lessons.Answer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_answers', to='students.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TakenExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='body',
        ),
        migrations.AddField(
            model_name='exercise',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='Student_answer',
        ),
        migrations.AddField(
            model_name='takenexercise',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_exercisezes', to='lessons.Exercise'),
        ),
        migrations.AddField(
            model_name='takenexercise',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_exercisezes', to='students.Student'),
        ),
        migrations.AddField(
            model_name='question',
            name='excercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lessons.Exercise'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='lessons.Question'),
        ),
    ]
