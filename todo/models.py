from django.db import models
from django.urls import reverse

class Task(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    completed   = models.BooleanField(default=False)
