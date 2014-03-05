from django.contrib import admin
from mobileserverstatus.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('version', 'status')

admin.site.register(Message, MessageAdmin)
