from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'is_completed')
    list_filter = ('client', 'is_completed')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'is_completed')
    list_filter = ('project', 'is_completed')
