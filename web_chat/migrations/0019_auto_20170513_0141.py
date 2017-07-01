# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0018_auto_20170513_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='record_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
