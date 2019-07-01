from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list = ['id', 'username', 'password', 'email', 'registered_time']


admin.site.register(Users, UsersAdmin)
