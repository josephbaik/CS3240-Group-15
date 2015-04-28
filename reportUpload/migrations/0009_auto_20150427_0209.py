# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0008_auto_20150426_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reportID',
            field=models.TextField(default='0000'),
            preserve_default=True,
        ),
    ]
