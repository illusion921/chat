# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_chat', '0021_sengimg_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sengimg',
            old_name='test',
            new_name='relationship',
        ),
    ]
