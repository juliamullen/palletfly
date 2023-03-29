from django.test         import TestCase
from django.urls         import reverse
from rest_framework.test import APIClient

from todo.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sample_task1 = {
            "title": "Shop for groceries",
            "description": "Buy red bell pepper, chickpeas, yellow onion",
            "completed": False
        }

        self.sample_task2 = {
            "title": "Make soup",
            "description": "Roast pepper and chickpeas, sautee onion, add stock",
            "completed": False
        }

    def test_create_task(self):
        response = self.client.post(reverse('task-list'), self.sample_task1, format='json')
        self.assertEqual(response.status_code, 201)

    def test_delete_task(self):
        t1 = Task.objects.create(**self.sample_task1)

        response = self.client.delete(reverse('task-detail', args=[t1.pk]))
        self.assertEqual(response.status_code, 204)

    def test_list_tasks(self):
        t1 = Task.objects.create(**self.sample_task1)
        t2 = Task.objects.create(**self.sample_task2)

        response = self.client.get(reverse('task-list'))
        response_titles = set([i.get('title') for i in response.json()])
        expected_titles = set([self.sample_task1['title'], self.sample_task2['title']])
        self.assertEqual(response_titles, expected_titles)

    def test_retrieve_task(self):
        t1 = Task.objects.create(**self.sample_task1)

        response = self.client.get(reverse('task-detail', args=[t1.pk]))
        self.assertEqual(response.json().get("title"), self.sample_task1['title'])
