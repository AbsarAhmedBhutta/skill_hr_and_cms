from django.db import models
from django.contrib.auth.models import User


# from employee.models import Employee


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.user}'


class ClientProjectProgress(models.Model):
    client_project = models.CharField(max_length=264)
    date = models.DateField()
    task = models.CharField(max_length=264)
    work_done = models.IntegerField()
    completed_by = models.CharField(max_length=264, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Client Project Progress"

    def __str__(self):
        return f"{self.client_project} - {self.date}"


class Budget(models.Model):
    PERIOD_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)


class FinancialTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('Payment', 'Payment'),
        ('Expense', 'Expense'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
