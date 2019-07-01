# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190611_2256'),
        ('todoitems', '0005_auto_20190615_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='userId',
            field=models.ForeignKey(default=None, to='users.Users'),
        ),
    ]
