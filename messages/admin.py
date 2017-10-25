from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ['body', 'user', 'channel']

admin.site.register(Message, MessageAdmin)
