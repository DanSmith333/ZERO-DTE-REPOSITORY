# Generated by Django 4.0.1 on 2022-02-02 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oscarrr', '0002_oscarrr_expiration_date_oscarrr_symbol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oscarrr',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='oscarrr',
            name='symbol',
        ),
    ]
