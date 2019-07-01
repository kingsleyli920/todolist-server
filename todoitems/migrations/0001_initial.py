# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('priority', models.IntegerField()),
                ('status', models.IntegerField()),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expired_time', models.DateTimeField()),
            ],
        ),
    ]
