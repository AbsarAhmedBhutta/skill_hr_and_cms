from django.contrib import admin
from .models import Client, ClientProjectProgress, Budget, FinancialTransaction
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')


@admin.register(ClientProjectProgress)
class ClientProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('client_project', 'date', 'task', 'work_done_progress', 'completed_by')
    list_filter = ('client_project', 'date', 'completed_by')

    def work_done_progress(self, obj):
        # Calculate the progress percentage based on the 'work_done' value and a maximum value
        max_work_done = 100  # Assuming 'work_done' is a percentage value, so the maximum is 100%
        work_done_percentage = min(obj.work_done, max_work_done)  # Ensure it doesn't exceed 100%

        # Determine the color based on the percentage range
        if work_done_percentage < 30:
            color = 'red'
        elif work_done_percentage < 50:
            color = 'yellow'
        elif work_done_percentage < 80:
            color = 'orange'
        else:
            color = 'green'

        # Determine the direction of the progress bar (left to right or right to left)
        if work_done_percentage < 50:
            progress_direction = 'left'
        else:
            progress_direction = 'right'

        # Format the progress bar HTML with inline style to change the color and direction
        progress_bar = f'<div class="progress">'
        progress_bar += f'<div class="progress-bar" style="width: {work_done_percentage}%; background-color: {color}; float: {progress_direction};">{work_done_percentage:.2f}%</div>'
        progress_bar += f'</div>'

        return format_html(progress_bar)

    work_done_progress.short_description = 'Work Done (%)'  # Column header in the admin list display


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'period')
    list_filter = ('client', 'period')


@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    list_display = ('client', 'transaction_type', 'amount', 'date', 'description')
    list_filter = ('client', 'transaction_type', 'date')
