# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoitems', '0002_auto_20190615_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 21, 2, 54, 399837, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
