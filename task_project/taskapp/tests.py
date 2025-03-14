from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task

# Create your tests here.

class TaskTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            created_by=self.user,
            assigned_to=self.user,
            status='pending'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.created_by, self.user)
        self.assertEqual(self.task.status, 'pending')

    def test_task_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskapp/task_list.html')
        self.assertContains(response, 'Test Task')

    def test_task_detail_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskapp/task_detail.html')
        self.assertContains(response, 'Test Task')

    def test_create_task(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'assigned_to': self.user.id,
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())
