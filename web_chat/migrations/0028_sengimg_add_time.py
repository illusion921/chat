# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0027_auto_20170520_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='sengimg',
            name='add_time',
            field=models.DateTimeField(default='2015-09-21 22:11:12', auto_now_add=True),
            preserve_default=False,
        ),
    ]
