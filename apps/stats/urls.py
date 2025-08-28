from django.urls import path
from apps.stats.views import StatisticsAPIView

urlpatterns = [
    path('stats/', StatisticsAPIView.as_view(), name='statistics'),
]
