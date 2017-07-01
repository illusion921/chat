# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0024_auto_20170519_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='msg_img',
            field=models.ImageField(upload_to=b'/python/chat/statics/imgs', blank=True),
        ),
        migrations.AlterField(
            model_name='sengimg',
            name='msg_img',
            field=models.FileField(upload_to=b'/python/chat/statics/imgs', blank=True),
        ),
    ]
