# Generated by Django 2.2.9 on 2020-07-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
