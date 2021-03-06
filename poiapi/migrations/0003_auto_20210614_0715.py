# Generated by Django 3.1.5 on 2021-06-14 07:15

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poiapi', '0002_auto_20210524_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='current_visitors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='peak_hours',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(-6.555760409044816, 106.7264194085899), geography=True, srid=4326),
        ),
    ]
