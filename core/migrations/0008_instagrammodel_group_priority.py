# Generated by Django 5.2.1 on 2025-05-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_trip_group_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagrammodel',
            name='group_priority',
            field=models.BooleanField(default=False),
        ),
    ]
