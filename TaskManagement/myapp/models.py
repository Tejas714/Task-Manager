from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    status = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()


class TaskRestore(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    status = models.CharField(max_length=50)
    deadline = models.DateTimeField()