# Generated by Django 4.1.3 on 2023-01-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_order_date_end_alter_order_date_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='choose_interval',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
