from datetime import date
from django.core.cache import cache
from rest_framework.test import APITestCase
from students.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CachingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass", role="Admin")
        self.client.login(username="testuser", password="testpass")
        self.student = Student.objects.create(user=self.user, dob=date(2000, 1, 1))

    def test_student_list_cache(self):
        url = "/students/students/"
        response1 = self.client.get(url)
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.get(url)
        self.assertEqual(len(response2.data), 1)

        cache.clear()
        response3 = self.client.get(url)
        self.assertEqual(len(response3.data), 2)