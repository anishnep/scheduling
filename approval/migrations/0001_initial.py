# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_request_id', models.PositiveIntegerField()),
                ('approved', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
