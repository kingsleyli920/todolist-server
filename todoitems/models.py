from django.db import models
import uuid
from django.utils import timezone
from users.models import Users

class ToDoItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, null=False)
    title = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=200, null=False)
    priority = models.IntegerField(null=False)
    status = models.IntegerField(null=False)
    userId = models.ForeignKey('users.Users', on_delete=models.CASCADE, default=None)
    updated_time = models.DateTimeField(default=timezone.now, null=False, )
    start_date = models.DateTimeField(null=False, default=timezone.now)
    expired_date = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.title
