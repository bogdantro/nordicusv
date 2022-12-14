# Generated by Django 4.1.3 on 2022-12-14 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_remove_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/user'),
            preserve_default=False,
        ),
    ]
