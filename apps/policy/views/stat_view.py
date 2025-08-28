
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.policy.models import PolicyModel, TranscationLedger
from apps.users.models.user_model import User

class StatisticsAPIView(APIView):
    def get(self, request):
        total_policies = PolicyModel.objects.count()
        total_users = User.objects.count()

        policies_last_30_days = PolicyModel.objects.filter(created_at__gte=timezone.now() - timedelta(days=30)).count()
        policies_last_7_days = PolicyModel.objects.filter(created_at__gte=timezone.now() - timedelta(days=7)).count()
        policies_today = PolicyModel.objects.filter(created_at__date=timezone.now().date()).count()

        policies = PolicyModel.objects.all()
        total_profit = 0
        total_loss = 0
        total_revenue = 0
        for policy in policies:
            transactions = TranscationLedger.objects.filter(policy=policy)

            for transaction in transactions:
                if transaction.type == 'payment':
                    total_revenue += transaction.amount
                else:
                    total_loss += transaction.amount

            total_profit += total_revenue - total_loss






        data = {
            "total_policies": total_policies,
            "total_users": total_users,
            "total_profit": total_profit,
            "total_revenue": total_revenue,
            "total_loss": total_loss,
            "30": [policies_last_30_days],
            "7": [policies_last_7_days],
            "1": [policies_today],
        }
        return Response(data)
