from django.db import models
from django.urls import reverse

class Task(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    completed   = models.BooleanField(default=False)


"""
    Task:
Design a simple Django model for a ToDo task. Include relevant fields such as title, description, and any other fields you deem necessary to store important information about the task.
Create a Django serializer for the ToDo task model using Django REST Framework.
Implement a viewset that handles the following actions for the ToDo task model:
i) List all tasks
ii) Create a new task
iii) Retrieve a specific task
iv) Delete a specific task
Set up routing for the viewset created in task 3. Use the default router provided by Django REST Framework to create the necessary URL patterns.

Test your API using tools such as Postman or CURL to ensure the endpoints are working as expected.

Note: You don't need to create a front-end for this assessment. The primary focus is on the back-end implementation using Django REST Framework.

Submission:
Provide a general guideline of the implementation, without going into specific details about model and serializer creation.

The preferred form of submission is by publishing a public repo on github with
your code and a README file explaining how to run the code.”

# Create your models here.
"""
