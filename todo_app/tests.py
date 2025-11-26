from django.test import TestCase
from django.urls import reverse
from .models import TodoItem
from datetime import date

class TodoItemModelTest(TestCase):
    def test_todo_creation(self):
        todo = TodoItem.objects.create(title="Test Todo", description="Test Description")
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.is_completed)

class TodoViewTest(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(title="Test Todo", description="Test Description")

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Todo',
            'description': 'New Description',
            'due_date': '2023-12-31'
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(TodoItem.objects.count(), 2)

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo_update', args=[self.todo.pk]), {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'due_date': '2023-12-31'
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo_delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.count(), 0)

    def test_todo_complete_view(self):
        response = self.client.get(reverse('todo_complete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_completed)
