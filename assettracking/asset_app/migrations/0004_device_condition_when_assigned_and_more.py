# Generated by Django 4.1.7 on 2023-03-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0003_remove_device_condition_when_assigned_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='condition_when_assigned',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='condition_when_returned',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='assigned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
