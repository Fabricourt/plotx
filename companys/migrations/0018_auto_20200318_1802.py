# Generated by Django 2.2.9 on 2020-03-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0017_auto_20200318_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='about_pic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='service_pic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
