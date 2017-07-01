# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0019_auto_20170513_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='SengImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'/root/PycharmProjects/chat/statics/imgs')),
                ('to_user', models.ForeignKey(related_name='img_to_user', to='web_chat.UserProfile')),
                ('user', models.ForeignKey(to='web_chat.UserProfile')),
            ],
        ),
    ]
