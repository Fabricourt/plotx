# Generated by Django 2.1.3 on 2019-12-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_plotinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('about_realtor', models.TextField(help_text='Enter a brief description of the Realtor.', max_length=1000)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('Instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('location', models.ManyToManyField(blank=True, help_text='Select The exact Location where this Company  is found in the choosen Town', to='catalog.Location')),
                ('plot', models.ManyToManyField(blank=True, help_text='Plots of interests to this buyer', to='catalog.Plot')),
                ('town', models.ManyToManyField(blank=True, help_text='Select the town where this realtor is found', to='catalog.Town')),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'phone'],
            },
        ),
        migrations.RemoveField(
            model_name='plotinstance',
            name='buyer',
        ),
    ]
