# Generated by Django 3.2 on 2021-05-04 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workshope', '0010_auto_20210504_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='attachments',
            field=models.FileField(default=django.utils.timezone.now, upload_to='replay_attachments'),
            preserve_default=False,
        ),
    ]
