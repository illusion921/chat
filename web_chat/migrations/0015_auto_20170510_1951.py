# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0014_auto_20170509_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='to_user',
            field=models.ForeignKey(related_name='to_user_record', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatrecord',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
