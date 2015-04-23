# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0003_auto_20150420_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='time',
            field=models.CharField(default='none', max_length=128),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.CharField(default='none', max_length=128),
            #preserve_default=True,
        ),
    ]
