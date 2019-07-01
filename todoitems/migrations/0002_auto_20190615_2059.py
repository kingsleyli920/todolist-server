# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoitems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='expired_time',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='expired_date',
            field=models.DateTimeField(null=True),
        ),
    ]
