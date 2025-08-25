from django.urls import path

from apps.policy.views.policy_view import (
    PolicyView,
    ClientView,
    InsuranceCompanyView,
    AgentView,
    TransactionLedgerView,
    TotalBalanceAgentView,
    PolicyDetailView,
)

urlpatterns = [
    path('policy/', PolicyView.as_view(), name='policy'),
    path('client/', ClientView.as_view(), name='client'),
    path('insurance-company/', InsuranceCompanyView.as_view(), name='insurance-company'),
    path('agent/', AgentView.as_view(), name='agent'),
    path('ledger/', TransactionLedgerView.as_view(), name='ledger'),
    path('total-balance/', TotalBalanceAgentView.as_view(), name='total-balance'),
    path('policy-detail/', PolicyDetailView.as_view(), name='policy-detail')
]