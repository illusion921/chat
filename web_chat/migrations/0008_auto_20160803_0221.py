# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_chat', '0007_auto_20160803_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('online', models.BooleanField(default=False)),
                ('friends', models.ManyToManyField(related_name='_userprofile_friends_+', to='web_chat.UserProfile')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('user_group', models.ManyToManyField(to='web_chat.UserGroup')),
            ],
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='admins',
            field=models.ManyToManyField(related_name='group_admins', to='web_chat.UserProfile', blank=True),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='founder',
            field=models.ForeignKey(to='web_chat.UserProfile'),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='group_name',
            field=models.ForeignKey(to='web_chat.UserGroup'),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to='web_chat.UserProfile', blank=True),
        ),
    ]
