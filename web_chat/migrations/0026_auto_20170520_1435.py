# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0025_auto_20170520_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sengimg',
            name='msg_img',
            field=models.FileField(upload_to=b'/python/chat/statics/files', blank=True),
        ),
    ]
