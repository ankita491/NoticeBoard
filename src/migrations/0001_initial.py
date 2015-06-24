# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=75)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_date', models.DateField()),
                ('event_timing', models.TimeField()),
                ('event_fees', models.IntegerField(default=0)),
                ('event_seats', models.IntegerField(default=36)),
                ('event_organiser_details', models.CharField(max_length=300)),
            ],
        ),
    ]
