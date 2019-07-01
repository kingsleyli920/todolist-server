from django.contrib import admin

from .models import ToDoItem


class ToDoItemAdmin(admin.ModelAdmin):
    list = ['id', 'title', 'content', 'priority', 'status', 'userId', 'updated_time', 'start_date', 'expired_time']


admin.site.register(ToDoItem, ToDoItemAdmin)
