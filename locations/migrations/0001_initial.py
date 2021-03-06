# Generated by Django 2.2.9 on 2020-04-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location_pic', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('lytube_video_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('location_video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
