from django.contrib import admin
from .models import Client, ClientProjectProgress, Budget, FinancialTransaction


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')


@admin.register(ClientProjectProgress)
class ClientProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('client_project', 'date', 'task', 'work_done', 'completed_by')
    list_filter = ('client_project', 'date', 'completed_by')


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'period')
    list_filter = ('client', 'period')


@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    list_display = ('client', 'transaction_type', 'amount', 'date', 'description')
    list_filter = ('client', 'transaction_type', 'date')
