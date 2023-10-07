from django.db import models
from django.contrib.auth.models import User
from project.models import Task  # Import Task from the projects app


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    father_name = models.CharField(max_length=264)
    address = models.CharField(max_length=264)
    tasks = models.ManyToManyField(Task, through='TaskAssignment')

    def __str__(self):
        return f'{self.user}|{self.tasks}'


class TaskAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.employee}|{self.task}'


class TaskSubmission(models.Model):
    task_assignment = models.ForeignKey(TaskAssignment, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    work_done = models.IntegerField()
    tell_whats_done = models.TextField()
    completed_by = models.CharField(max_length=264, null=True, blank=True)

    def __str__(self):
        return f'{self.task_assignment}|{self.submission_date}|{self.work_done}'
