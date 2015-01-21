# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_joinfriends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinfriends',
            name='email',
        ),
        migrations.RemoveField(
            model_name='joinfriends',
            name='emailall',
        ),
        migrations.RemoveField(
            model_name='joinfriends',
            name='friends',
        ),
        migrations.DeleteModel(
            name='JoinFriends',
        ),
    ]
