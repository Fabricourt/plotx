# Generated by Django 2.2.9 on 2020-06-07 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_remove_teacher_subjects'),
        ('subjects', '0009_auto_20200603_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.Teacher'),
        ),
    ]