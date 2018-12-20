# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.TextField(max_length=20)),
                ('lastName', models.TextField(max_length=20)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('potfolioWebsite', models.TextField(max_length=50)),
                ('jobPosition', models.TextField(max_length=20)),
                ('salaryExpectations', models.TextField(max_length=20)),
                ('expectedJoining', models.DateField()),
                ('phone', models.TextField(max_length=15)),
                ('relocation', models.TextField(max_length=20)),
                ('lastCompany', models.TextField(max_length=20)),
                ('uploadResume', models.FileField(upload_to=b'profiles/')),
                ('comments', models.TextField(max_length=50)),
                ('status', models.TextField(default=b'pending', max_length=10)),
                ('appliedDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
