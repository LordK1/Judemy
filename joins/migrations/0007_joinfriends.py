# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0006_auto_20141231_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinFriends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.OneToOneField(related_name='Sharer', to='joins.Join')),
                ('emailall', models.ForeignKey(related_name='emailall', to='joins.Join')),
                ('friends', models.ManyToManyField(related_name='friends', null=True, to='joins.Join', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
