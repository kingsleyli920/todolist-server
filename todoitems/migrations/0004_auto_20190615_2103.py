# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoitems', '0003_auto_20190615_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='expired_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
