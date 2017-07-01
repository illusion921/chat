# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0015_auto_20170510_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='to_user',
            field=models.ForeignKey(related_name='to_user_record', to='web_chat.UserProfile'),
        ),
        migrations.AlterField(
            model_name='chatrecord',
            name='user',
            field=models.ForeignKey(to='web_chat.UserProfile'),
        ),
    ]
