# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0008_auto_20160803_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='founder',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
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
            name='ChatGroup',
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
