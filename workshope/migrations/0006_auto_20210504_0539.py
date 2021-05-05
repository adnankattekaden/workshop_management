# Generated by Django 3.2 on 2021-05-04 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workshope', '0005_remove_jobcard_tracking_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcard',
            name='datetime',
        ),
        migrations.AddField(
            model_name='jobcard',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobcard',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]