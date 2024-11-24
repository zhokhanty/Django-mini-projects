from django.core.cache import cache
from requests import Response
from rest_framework.viewsets import ModelViewSet
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
import logging
from rest_framework.filters import OrderingFilter
from .models import Course
from .serializers import CourseSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger('custom')

class CourseFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['name']

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ['name', 'instructor']
    ordering = ['name']

    def perform_create(self, serializer):
        course = serializer.save()
        logger.info(f"Course {course.name} created.")

    def enroll_student(self, student, course):
        logger.info(f"Student {student.name} enrolled in course {course.name}.")
    
    def list(self, request, *args, **kwargs):
        cached_courses = cache.get('courses_list')

        if cached_courses is not None:
            return Response(cached_courses)

        response = super().list(request, *args, **kwargs)
        cache.set('courses_list', response.data, timeout=300)

        return response

class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer