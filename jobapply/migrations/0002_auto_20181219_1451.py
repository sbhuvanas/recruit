# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='firstName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='jobPosition',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='lastCompany',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='lastName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='potfolioWebsite',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='relocation',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='salaryExpectations',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='status',
            field=models.CharField(default=b'pending', max_length=10),
        ),
    ]
