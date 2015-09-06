# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='has_work',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
