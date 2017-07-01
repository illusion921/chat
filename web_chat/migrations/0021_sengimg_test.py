# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0020_sengimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='sengimg',
            name='test',
            field=models.CharField(default=b'abc', max_length=40),
        ),
    ]
