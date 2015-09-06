# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_id', models.IntegerField(verbose_name=b'Employee-ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('is_supervisor', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(default=b'<<add your company name>>', max_length=120)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_date', models.DateField()),
                ('has_work', models.BooleanField()),
                ('start_time', models.CharField(max_length=120, blank=True)),
                ('end_time', models.CharField(max_length=120, blank=True)),
                ('notes', models.CharField(max_length=120, null=True, verbose_name=b'Note', blank=True)),
                ('employee', models.ForeignKey(to='timetable.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_date', models.DateField()),
                ('request_type', models.IntegerField(default=1, choices=[(1, b'work day'), (2, b'free day')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'pending'), (2, b'accepted'), (3, b'rejected')])),
                ('checked', models.BooleanField(default=False)),
                ('approved_by', models.CharField(max_length=50, null=True, blank=True)),
                ('requested_by', models.ForeignKey(related_name='work_request', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='employer',
            field=models.ForeignKey(default=1, to='timetable.Employer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set([('emp_id', 'employer')]),
        ),
    ]
