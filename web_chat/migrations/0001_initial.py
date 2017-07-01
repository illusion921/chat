# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(unique=True, max_length=16)),
                ('members_limit', models.IntegerField(default=200)),
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
                ('user_group', models.ManyToManyField(to='web_chat.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='admins',
            field=models.ManyToManyField(related_name='group_admins', to='web_chat.UserProfile', blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='founder',
            field=models.ForeignKey(to='web_chat.UserProfile'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to='web_chat.UserProfile', blank=True),
        ),
    ]
