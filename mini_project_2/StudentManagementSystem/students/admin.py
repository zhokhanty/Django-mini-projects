from django.contrib import admin

from courses.models import Course, Enrollment

admin.site.register(Course)
admin.site.register(Enrollment)