# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0029_auto_20170521_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('is_new', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=False)),
                ('add_user', models.ForeignKey(related_name='confirm_add_user', to='web_chat.UserProfile')),
                ('user', models.ForeignKey(to='web_chat.UserProfile')),
            ],
        ),
    ]
