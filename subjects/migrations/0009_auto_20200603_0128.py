# Generated by Django 2.2.9 on 2020-06-02 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_auto_20200526_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['subject_name'], 'verbose_name': 'Learning_area', 'verbose_name_plural': 'Learning_areas'},
        ),
    ]
