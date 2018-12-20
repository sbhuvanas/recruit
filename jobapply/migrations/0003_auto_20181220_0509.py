# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0002_auto_20181219_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='comments',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='expectedJoining',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='firstName',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='jobPosition',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='lastCompany',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='lastName',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='potfolioWebsite',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='relocation',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='salaryExpectations',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='status',
            field=models.CharField(default=b'pending', max_length=10, choices=[[b'pending', b'Pending'], [b'accepted', b'Accepted'], [b'rejected', b'Rejected']]),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='uploadResume',
            field=models.FileField(null=True, upload_to=b'profiles/', blank=True),
        ),
    ]
