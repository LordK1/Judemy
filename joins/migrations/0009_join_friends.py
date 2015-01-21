# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0008_auto_20141231_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friends',
            field=models.ForeignKey(related_name='referral', blank=True, to='joins.Join', null=True),
            preserve_default=True,
        ),
    ]
