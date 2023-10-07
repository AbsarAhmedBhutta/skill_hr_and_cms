from django.contrib import admin

from client.models import ClientProjectProgress
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
    list_display = ('task_assignment', 'submission_date', 'work_done_in_percentage', 'tell_whats_done', 'completed_by')
    list_filter = ('task_assignment', 'submission_date', 'completed_by')

    def save_model(self, request, obj, form, change):
        # Automatically set the 'completed_by' field to the username of the currently logged-in user
        obj.completed_by = request.user.username  # Assign the username

        # Copy relevant data into ClientProjectProgress
        client_project_name = obj.task_assignment.task.project.name
        submission_date = obj.submission_date
        task_name = obj.task_assignment.task.name

        # Use update_or_create to avoid duplicates
        client_project_progress, created = ClientProjectProgress.objects.update_or_create(
            client_project=client_project_name,
            date=submission_date,
            task=task_name,
            completed_by=request.user.username,  # Use the username
            defaults={'work_done': obj.work_done_in_percentage}
        )

        # You don't need to update the 'work_done' field manually
        # It will be updated automatically by update_or_create

        super().save_model(request, obj, form, change)
