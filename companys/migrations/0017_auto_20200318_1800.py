# Generated by Django 2.2.9 on 2020-03-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0016_auto_20200318_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_pic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
