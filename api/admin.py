from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, GameMode, Record

admin.site.register(User)
admin.site.register(GameMode)
admin.site.register(Record)

admin.site.unregister(Group)
