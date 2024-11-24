from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from analytics.models import APIRequestLog, PopularCourse

class AnalyticsView(APIView):
    def get(self, request):
        most_active_users = APIRequestLog.objects.values('user__username').annotate(requests=Count('id')).order_by('-requests')[:5]
        most_popular_courses = PopularCourse.objects.values('course__name').annotate(count=Count('id')).order_by('-access_count')[:5]
        return Response({
            "most_active_users": most_active_users,
            "most_popular_courses": most_popular_courses
        })