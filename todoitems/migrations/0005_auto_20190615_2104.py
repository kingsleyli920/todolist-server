# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoitems', '0004_auto_20190615_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
