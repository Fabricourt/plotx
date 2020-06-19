# Generated by Django 2.2.9 on 2020-06-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0014_remove_class_class_students'),
        ('students', '0007_remove_student_classname'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='classname', to='classes.Class'),
        ),
    ]
