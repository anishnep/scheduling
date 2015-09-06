# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20150619_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=70, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='has_got_password',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
