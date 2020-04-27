# Generated by Django 2.2.9 on 2020-04-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0002_bg_color_2_bg_color_3'),
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='bg_color_2',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='colors.Bg_color_2'),
        ),
        migrations.AddField(
            model_name='business',
            name='bg_color_3',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='colors.Bg_color_3'),
        ),
    ]