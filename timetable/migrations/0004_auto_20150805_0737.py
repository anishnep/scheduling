# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20150619_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='work',
            name='worker_position',
            field=models.CharField(default=b'Normal', max_length=50),
            preserve_default=True,
        ),
    ]
