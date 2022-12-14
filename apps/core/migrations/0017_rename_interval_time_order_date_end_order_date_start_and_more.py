# Generated by Django 4.1.3 on 2023-01-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_order_custom_cords_11_order_custom_cords_12_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='interval_time',
            new_name='date_end',
        ),
        migrations.AddField(
            model_name='order',
            name='date_start',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='friday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='monday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='saturday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='sunday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='thursday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tuesday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='wednesday',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
