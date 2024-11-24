from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class APIRequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

class PopularCourse(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    access_count = models.PositiveIntegerField(default=0)