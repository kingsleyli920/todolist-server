from rest_framework import serializers
from .models import ToDoItem
from users.serializers import UsersSerializer

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('id', 'title', 'content', 'priority', 'status', 'userId', 'updated_time', 'start_date', 'expired_date')