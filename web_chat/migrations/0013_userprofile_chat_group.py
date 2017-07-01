# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0012_auto_20160803_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='chat_group',
            field=models.ManyToManyField(to='web_chat.ChatGroup'),
        ),
    ]
