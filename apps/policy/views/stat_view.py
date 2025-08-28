
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.policy.models import PolicyModel, TranscationLedger, AgentModel, ClientModel
from apps.policy.utils import get_total_profit


class StatisticsAPIView(APIView):
    def get(self, request):
        total_policies = PolicyModel.objects.count()
        total_agents = AgentModel.objects.count()
        total_clients = ClientModel.objects.count()

        policies_last_30_days = PolicyModel.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=30))
        policies_last_7_days = PolicyModel.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=7))
        policies_today = PolicyModel.objects.filter(
            created_at=timezone.now().date())

        policies = PolicyModel.objects.all()

        total_profit, total_revenue, total_loss = get_total_profit(policies)
        profit_30, revenue_30, loss_30 = get_total_profit(
            policies_last_30_days)
        profit_7, revenue_7, loss_7 = get_total_profit(policies_last_7_days)
        profit_1, revenue_1, loss_1 = get_total_profit(policies_today)

        data = {
            "total_policies": total_policies,
            "total_agents": total_agents,
            "total_clients": total_clients,
            "total_profit": total_profit,
            "total_revenue": total_revenue,
            "total_loss": total_loss,
            "30": {
                "policy_count": policies_last_30_days.count(),
                "profit": profit_30,
                "revenue": revenue_30,
                "loss": loss_30
            },
            "7": {
                "policy_count": policies_last_7_days.count(),
                "profit": profit_7,
                "revenue": revenue_7,
                "loss": loss_7
            },
            "1": {
                "policy_count": policies_today.count(),
                "profit": profit_1,
                "revenue": revenue_1,
                "loss": loss_1
            },
        }
        return Response(data)
