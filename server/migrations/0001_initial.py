# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('registered_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
