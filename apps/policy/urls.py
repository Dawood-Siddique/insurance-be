from django.urls import path

from apps.policy.views.policy_view import (
    PolicyView,
    ClientView,
    InsuranceCompanyView,
    AgentView,
)

urlpatterns = [
    path('policy/', PolicyView.as_view(), name='policy'),
    path('client/', ClientView.as_view(), name='client'),
    path('insurance-company/', InsuranceCompanyView.as_view(), name='insurance-company'),
    path('agent/', AgentView.as_view(), name='agent'),
]