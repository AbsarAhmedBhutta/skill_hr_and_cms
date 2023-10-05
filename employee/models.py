from django.db import models
from django.core.validators import MaxValueValidator

from client.models import Project


class Employee(models.Model):
    name = models.CharField(max_length=100)
    # Add more employee-related fields


class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    progress = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
