# Generated by Django 2.2.9 on 2020-03-05 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_auto_20200305_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bg_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Text_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='color',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.AddField(
            model_name='company',
            name='bg_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Bg_color'),
        ),
        migrations.AddField(
            model_name='company',
            name='text_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Text_color'),
        ),
    ]