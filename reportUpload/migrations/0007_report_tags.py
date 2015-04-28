# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportUpload', '0006_auto_20150425_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='tags',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
