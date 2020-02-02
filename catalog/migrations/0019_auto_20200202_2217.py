# Generated by Django 2.2.9 on 2020-02-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_company_company_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='realtor',
            field=models.ManyToManyField(blank=True, help_text='realtors', to='catalog.Realtor'),
        ),
        migrations.AddField(
            model_name='realtor',
            name='statement',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
