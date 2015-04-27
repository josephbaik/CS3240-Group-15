# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0009_auto_20150427_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='enckey',
            field=models.CharField(max_length=516, default=''),
            preserve_default=True,
        ),
    ]
