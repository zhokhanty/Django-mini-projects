from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status
from students.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentViewTests(APITestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(username="student", password="studentpass", role="Student")
        self.student = Student.objects.create(user=self.student_user, dob=date(2000, 1, 1))

        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass", role="Admin")
        self.client.login(username="admin", password="adminpass")

    def test_get_student_details(self):
        url = f"/students/students/{self.student.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student(self):
        url = f"/students/students/{self.student.id}/"
        data = {"name": "Updated Name"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()