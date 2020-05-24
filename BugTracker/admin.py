from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from BugTracker.models import MyUser, Ticket

# Register your models here.
admin.site.register(MyUser, UserAdmin)
admin.site.register(Ticket)
