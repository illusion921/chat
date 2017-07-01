# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0028_sengimg_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='record_time',
            field=models.CharField(max_length=100),
        ),
    ]
