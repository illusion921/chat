# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0022_auto_20170513_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_group',
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='admins',
            field=models.ManyToManyField(related_name='group_admins', to='web_chat.UserProfile'),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to='web_chat.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='chat_group',
            field=models.ManyToManyField(to='web_chat.ChatGroup', blank=True),
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]
