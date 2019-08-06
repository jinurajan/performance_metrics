# Generated by Django 2.2.4 on 2019-08-05 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('channel', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=10)),
                ('impressions', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
                ('installs', models.IntegerField(default=0)),
                ('spend', models.FloatField(default=0)),
                ('revenue', models.FloatField(default=0)),
            ],
        ),
    ]
