# Generated by Django 2.2.9 on 2020-03-18 14:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0008_auto_20200318_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='about_business',
            field=ckeditor.fields.RichTextField(help_text='Max 200 words', max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='about_pic',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='business',
            name='business_pic',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='business',
            name='contact_person',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, default='logo.png', upload_to='logos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='business',
            name='service_pic',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='business',
            name='services',
            field=ckeditor.fields.RichTextField(help_text='Max 200 words', max_length=1500, null=True),
        ),
    ]