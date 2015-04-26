# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0007_report_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reportID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.CharField(max_length=128, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='longd',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='short',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.CharField(max_length=128, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='url',
            field=models.URLField(default=''),
            preserve_default=True,
        ),
    ]
