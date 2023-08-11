from django.contrib import admin
from .models import Message, Room, Conversation

# Register your models here.
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Conversation)
