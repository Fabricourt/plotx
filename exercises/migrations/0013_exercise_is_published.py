# Generated by Django 2.2.9 on 2020-06-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0012_auto_20200608_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
