# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(unique=True, max_length=16)),
                ('members_limit', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='group',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='group',
            name='founder',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_group',
            field=models.ManyToManyField(to='web_chat.UserGroup'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='admins',
            field=models.ManyToManyField(related_name='group_admins', to='web_chat.UserProfile', blank=True),
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='founder',
            field=models.ForeignKey(to='web_chat.UserProfile'),
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to='web_chat.UserProfile', blank=True),
        ),
    ]
