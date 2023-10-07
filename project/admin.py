from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'is_completed')
    list_filter = ('client', 'is_completed')



