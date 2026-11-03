from django.contrib import admin
from .models import Job, Machine, Time

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'required_quantity', 'deadline')
    list_filter = ('status',)
    search_fields = ('name', 'description')
@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'code', 'description')
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('worker', 'machine', 'job', 'status', 'timestamp')
    list_filter = ('status',"machine", "job")
    search_fields = ('worker__full_name', 'machine__name', 'job__name')