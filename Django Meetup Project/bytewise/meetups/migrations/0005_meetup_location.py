# Generated by Django 5.0.2 on 2024-07-17 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_remove_meetup_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
            preserve_default=False,
        ),
    ]
