from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

class StudentFilter(filters.FilterSet):
    dob = filters.DateFilter()
    registration_date = filters.DateFilter()

    class Meta:
        model = Student
        fields = ['dob', 'registration_date']

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Teacher':
            return Student.objects.filter(course__instructor=user).distinct()
        return super().get_queryset()