from rest_framework.views import APIView
from rest_framework.response import Response
from apps.policy.models import PolicyModel
from apps.users.models.user_model import User
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

class StatisticsAPIView(APIView):
    def get(self, request):
        total_policies = PolicyModel.objects.count()
        total_users = User.objects.count()

        policy_status_breakdown = PolicyModel.objects.values('status').annotate(count=Count('status'))

        thirty_days_ago = timezone.now() - timedelta(days=30)
        policies_last_30_days = PolicyModel.objects.filter(created_at__gte=thirty_days_ago).count()

        data = {
            "total_policies": total_policies,
            "total_users": total_users,
            "policy_status_breakdown": list(policy_status_breakdown),
            "policies_created_last_30_days": policies_last_30_days,
        }
        return Response(data)
