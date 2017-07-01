# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0013_userprofile_chat_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('send_type', models.CharField(max_length=20)),
                ('record_time', models.DateField()),
                ('msg_data', models.CharField(max_length=100)),
                ('msg_img', models.ImageField(upload_to=b'/root/PycharmProjects/chat/statics/imgs', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(unique=True, max_length=16),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='to_user',
            field=models.ForeignKey(related_name='to_user_record', to='web_chat.UserProfile'),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='user',
            field=models.ForeignKey(to='web_chat.UserProfile'),
        ),
    ]
