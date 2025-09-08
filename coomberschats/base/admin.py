from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

admin.site.register(Room) # register the Room model to be accessible in the admin panel
admin.site.register(Topic) # register the Topic model to be accessible in the admin panel
admin.site.register(Message) # register the Message model to be accessible in the admin panel