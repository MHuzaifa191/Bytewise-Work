# Generated by Django 5.0.2 on 2024-07-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0008_participant_meetup_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-04-1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
    ]
