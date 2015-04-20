# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0002_report_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='longd',
            field=models.TextField(default='none'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='short',
            field=models.TextField(default='none'),
            preserve_default=True,
        ),
    ]
