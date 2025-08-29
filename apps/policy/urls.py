from django.urls import path

from apps.policy.views.policy_view import (
    PolicyView,
    ClientView,
    InsuranceCompanyView,
    AgentView,
    TransactionLedgerView,
    TotalBalanceAgentView,
    PolicyDetailView,
    CancelPolicyView,
)

from apps.policy.views.stat_view import StatisticsAPIView

stat_url = [
    path('stats/', StatisticsAPIView.as_view(), name='statistics'),
]

policy_url = [
    path('policy/', PolicyView.as_view(), name='policy'),
    path('client/', ClientView.as_view(), name='client'),
    path('insurance-company/', InsuranceCompanyView.as_view(), name='insurance-company'),
    path('agent/', AgentView.as_view(), name='agent'),
    path('ledger/', TransactionLedgerView.as_view(), name='ledger'),
    path('total-balance/', TotalBalanceAgentView.as_view(), name='total-balance'),
    path('policy-detail/', PolicyDetailView.as_view(), name='policy-detail'),
    path('cancel-policy/', CancelPolicyView.as_view(), name='cancel-policy'),
]

urlpatterns = [
    *stat_url, 
    *policy_url
]