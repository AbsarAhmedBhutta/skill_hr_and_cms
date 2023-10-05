from django.contrib import admin
from .models import Employee, Task


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'project', 'employee', 'completed', 'progress',)
    list_filter = ('project', 'completed',)
    search_fields = ('description', 'employee__name',)
