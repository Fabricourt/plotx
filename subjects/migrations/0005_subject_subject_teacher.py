# Generated by Django 2.2.9 on 2020-05-23 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0004_subject_hover_border_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subject_teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
