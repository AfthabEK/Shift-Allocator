# Generated by Django 4.2.5 on 2023-09-19 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datewindow',
            name='end_date',
        ),
    ]
