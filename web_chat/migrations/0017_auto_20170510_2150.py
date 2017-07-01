# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0016_auto_20170510_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='user',
            field=models.ForeignKey(related_name='user_record', to='web_chat.UserProfile'),
        ),
    ]
