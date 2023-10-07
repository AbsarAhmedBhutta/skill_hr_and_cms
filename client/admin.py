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

        # Format the progress bar HTML with the percentage symbol and use mark_safe
        progress_bar = '<div class="progress">' \
                       '<div class="progress-bar" style="width:;">{:.2f}%</div>' \
                       '</div>'.format(work_done_percentage, work_done_percentage)

        return mark_safe(progress_bar)

    work_done_progress.short_description = 'Work Done (%)'  # Column header in the admin


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'period')
    list_filter = ('client', 'period')


@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    list_display = ('client', 'transaction_type', 'amount', 'date', 'description')
    list_filter = ('client', 'transaction_type', 'date')
