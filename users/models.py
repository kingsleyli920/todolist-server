from django.db import models
import uuid
from django.utils import timezone


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, null=False)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=500, null=False)
    email = models.CharField(max_length=500, null=False)
    registered_time = models.DateTimeField(default=timezone.now, null=False, )

    def __str__(self):
        return self.username
