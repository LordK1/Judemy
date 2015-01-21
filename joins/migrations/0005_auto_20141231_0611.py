# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_join_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default=b'ABC', unique=True, max_length=120),
            preserve_default=True,
        ),
    ]
