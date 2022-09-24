# Generated by Django 3.2 on 2022-09-23 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0002_auto_20220924_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelfile',
            name='animal_name',
            field=models.CharField(default='', max_length=30, verbose_name='動物名'),
        ),
        migrations.AddField(
            model_name='modelfile',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='modelfile',
            name='proba',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='modelfile',
            name='registered_date',
            field=models.DateField(default=datetime.date(2022, 9, 24)),
        ),
        migrations.AlterField(
            model_name='modelfile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]