# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20150805_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='worker_position',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
