# Generated by Django 2.2.9 on 2020-06-03 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_auto_20200602_2111'),
        ('exercises', '0008_auto_20200603_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='classname',
        ),
        migrations.AddField(
            model_name='answer',
            name='classname',
            field=models.ForeignKey(blank=True, help_text='Pick your class', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ansclass', to='classes.Class'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='subjects.Subject'),
        ),
    ]
