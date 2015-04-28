# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0011_auto_20150427_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='folder',
            field=models.TextField(max_length=516, default=''),
            preserve_default=True,
        ),
    ]
