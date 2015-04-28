# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0004_auto_20150420_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.TextField(default='none'),
            preserve_default=True,
        ),
    ]
