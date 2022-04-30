# Generated by Django 4.0.1 on 2022-02-03 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oscarrr', '0003_remove_oscarrr_expiration_date_remove_oscarrr_symbol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oscarrr',
            name='oscarrr_text',
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='BF',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='CN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='IC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='IF',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='UF',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='es_option',
            field=models.CharField(default=' (EOM) /EW22:XCE ', max_length=17),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='es_spx_difference',
            field=models.IntegerField(default=-10),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='es_symbol',
            field=models.CharField(default='/ESH22:XCME 1/50', max_length=16),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='expiration_date',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='max_base',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='max_distance',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='max_loss',
            field=models.IntegerField(default=-150),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='min_R2R',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='min_base',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='min_distance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oscarrr',
            name='symbol',
            field=models.CharField(default='SPX', max_length=6, verbose_name='SPX'),
        ),
    ]
