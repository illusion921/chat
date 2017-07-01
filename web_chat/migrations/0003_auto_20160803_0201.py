# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0002_auto_20160803_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qqgroup',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='qqgroup',
            name='founder',
        ),
        migrations.RemoveField(
            model_name='qqgroup',
            name='members',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_group',
        ),
        migrations.DeleteModel(
            name='QQGroup',
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
