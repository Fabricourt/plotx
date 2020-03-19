# Generated by Django 2.2.9 on 2020-03-15 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0038_auto_20200314_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plot',
            options={'ordering': ['list_date']},
        ),
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
