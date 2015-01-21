# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.IPAddressField(default=b'ABC'),
            preserve_default=True,
        ),
    ]
