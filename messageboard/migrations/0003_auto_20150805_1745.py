# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageboard', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(related_name='comments', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
