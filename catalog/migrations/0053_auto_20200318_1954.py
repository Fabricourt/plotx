# Generated by Django 2.2.9 on 2020-03-18 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0052_auto_20200318_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='border_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Border_color'),
        ),
        migrations.AlterField(
            model_name='company',
            name='hover_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Hover_color'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='border_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Border_color'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='hover_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Hover_color'),
        ),
    ]
