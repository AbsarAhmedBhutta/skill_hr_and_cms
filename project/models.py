from django.db import models
from client.models import Client  # Import Client model from the client app


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    requirements = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.client}|{self.name}'


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.project}|{self.name}'
