from django.contrib import admin

from main.models import *
from django.contrib.auth.models import Group, User

admin.site.register(Session)

admin.site.unregister(Group)
admin.site.unregister(User)