# Generated by Django 5.0.2 on 2024-07-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0009_meetup_date_meetup_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='organizer',
            field=models.EmailField(max_length=254),
        ),
    ]
