# Generated by Django 3.0 on 2020-01-24 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20200123_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='existingdata',
            name='wind_deg',
        ),
    ]
