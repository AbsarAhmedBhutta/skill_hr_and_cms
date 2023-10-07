from django.contrib import admin
from .models import Employee, TaskAssignment, TaskSubmission


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'task', 'is_completed')
    list_filter = ('employee', 'task', 'is_completed')


@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ('task_assignment', 'submission_date', 'work_done', 'tell_whats_done', 'completed_by')
    list_filter = ('task_assignment', 'submission_date', 'completed_by')

    def save_model(self, request, obj, form, change):
        # Automatically set the 'completed_by' field to the currently logged-in user
        obj.completed_by = request.user
        super().save_model(request, obj, form, change)
