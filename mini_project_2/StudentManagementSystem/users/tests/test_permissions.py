from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class RolePermissionsTests(APITestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(username="student", password="studentpass", role="Student")
        self.teacher_user = User.objects.create_user(username="teacher", password="teacherpass", role="Teacher")
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass", role="Admin")

    def test_student_restricted_access(self):
        self.client.login(username="student", password="studentpass")
        response = self.client.get("/courses/courses")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_access(self):
        self.client.login(username="admin", password="adminpass")
        response = self.client.get("/courses/courses")
        self.assertEqual(response.status_code, status.HTTP_200_OK)