# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0026_auto_20170520_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sengimg',
            name='relationship',
        ),
        migrations.AddField(
            model_name='sengimg',
            name='file_name',
            field=models.CharField(default=b'files', max_length=100),
        ),
    ]
