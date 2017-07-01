# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0010_auto_20160803_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_group',
            field=models.ManyToManyField(to='web_chat.UserGroup'),
        ),
    ]
