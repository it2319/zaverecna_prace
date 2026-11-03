from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import WorkerProfile

class WorkerProfileInline(admin.StackedInline):
    model = WorkerProfile
    can_delete = False
    fk_name = 'user_id'
    max_num = 1
    fields = ('employee_id', 'full_name',)

class UserAdmin(BaseUserAdmin):
    inlines = (WorkerProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
