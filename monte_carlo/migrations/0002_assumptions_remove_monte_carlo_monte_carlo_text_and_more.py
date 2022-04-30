# Generated by Django 4.0.1 on 2022-02-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monte_carlo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assumptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assumption_number', models.IntegerField(default=0)),
                ('hit_rate', models.IntegerField(default=20)),
                ('low_end', models.IntegerField(default=0)),
                ('high_end', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='monte_carlo',
            name='monte_carlo_text',
        ),
        migrations.AddField(
            model_name='monte_carlo',
            name='begin_balance',
            field=models.FloatField(default=10000),
        ),
        migrations.AddField(
            model_name='monte_carlo',
            name='position_size',
            field=models.FloatField(default=1.5),
        ),
    ]
